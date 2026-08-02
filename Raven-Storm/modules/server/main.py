# 2020
# The Raven-Storm Toolkit was programmed and developed by Taguar258.
# The Raven-Storm Toolkit is published under the MIT Licence.
# The Raven-Storm Toolkit is based on the CLIF-Framework.
# The CLIF-Framework is programmed and developed by Taguar258.
# The CLIF-Framework is published under the MIT Licence.

from os import system
from time import sleep

import flask
import requests
from CLIF_Framework.framework import console  # noqa: I900
from CLIF_Framework.framework import event  # noqa: I900
from CLIF_Framework.framework import module  # noqa: I900
from CLIF_Framework.framework import tools  # noqa: I900
from flask import request

try:
	import readline  # noqa: F401
except Exception:  # noqa: S110
	pass


event = event()
tools = tools()


class Main:
	def __init__(selfie, console):  # noqa: N805
		global var
		global self
		self = selfie
		var = console  # noqa: VNE002

		# Colors
		var.C_None = "\x1b[0;39m"
		var.C_Bold = "\x1b[1;39m"
		var.C_Green = "\x1b[32m"
		var.C_Violet = "\x1b[34m"
		var.C_Dark_Blue = "\x1b[35m"
		var.C_Red = "\x1b[31m"
		var.C_Yellow = "\x1b[33m"
		var.C_Cyan = "\x1b[36m"

		var.host = "127.0.0.1"
		var.port = "5261"
		var.password = ""

	def banner(self):  # """ + self.generate_quote() + """
		banner_fire_color = var.C_Cyan
		banner_middle_color = var.C_Violet
		banner_bottom_color = var.C_Dark_Blue
		banner_logo = ("""C_Bo-----------------------------------------------------------C_W
C_FIRE (
 )\\ )                                 )
(()/(    )   )      (              ( /(      (       )
 /(_))( /(  /((    ))\\  (      (   )\\()) (   )(     (
(C_MID_C_FIRE))  )(_))(_))\\  /((_) )\\ )   )\\ (C_MID_C_FIRE))/  )\\ (()\\    )\\  'C_MID
| _ \\C_FIRE((C_MID_C_FIRE)C_MID_ _C_FIRE)((C_MID_C_FIRE)(C_MID_C_FIRE))  C_MID_C_FIRE(C_MID_C_FIRE/(  ((C_MID_C_FIRE)C_MID| |C_FIRE  ((C_MID_C_FIRE) ((C_MID_C_FIRE) C_MID_C_FIRE((C_MID_C_FIRE))C_MID
|   // _` |\\ V / / -_)| ' \\)) (_-<|  _|/ _ \\| '_|| '  \\C_FIRE()C_BOT
|_|_\\\\__,_| \\_/  \\___||_||_|  /__/ \\__|\\___/|_|  |_|_|_|C_W

----- The server module for the remote DDos attacks. -----

C_Bo-----------------------------------------------------------C_W""")
		banner_logo = banner_logo.replace("C_W", var.C_None)
		banner_logo = banner_logo.replace("C_Bo", var.C_Bold)
		banner_logo = banner_logo.replace("C_FIRE", banner_fire_color)
		banner_logo = banner_logo.replace("C_MID", banner_middle_color)
		banner_logo = banner_logo.replace("C_BOT", banner_bottom_color)
		print(banner_logo)

	@event.event
	def on_ready():
		system("clear || cls")
		self.banner()
		self._add_commands()
		self.help()

	@event.event
	def on_command_not_found(command):
		print("")
		print("您输入的命令不存在。")
		print("")

	def exit_console(self):
		print("祝您有美好的一天。")
		quit()

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")
		event.commands(self.help, "help")
		event.parser(self.run_debug_arg, "$")
		event.parser(self.run_shell_arg, ".")
		event.help(["exit", "quit", "e", "q"], "退出 Raven-Storm。")
		event.help("help", "查看所有命令。")
		event.help(".", "运行 shell 命令。")
		event.help("clear", "清除屏幕。")
		event.help("host", "输入主机 IP。")
		event.help("port", "输入主机端口。")
		event.help("password", "设置密码。")
		event.help("run", "启动服务器。")

	def run_shell(self, command):
		system(command)

	def run_shell_arg(self, command):
		return tools.arg("输入 shell 命令：", ". ", command)
		print("", end="")

	def debug(self, command):
		eval(command)

	def run_debug_arg(self, command):
		return tools.arg("输入调试命令：", "$ ", command)
		print("", end="")

	def help(self):
		event.help_title("\x1b[1;39mServer Help:\x1b[0;39m")
		tools.help("|-- ", " :: ", event)
		print("")

	@event.command
	def clear():
		system("clear || cls")

	@event.event
	def on_command():
		print("", end="")

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
		self.exit_console()

	@event.event
	def on_command(command):
		if var.session[0][0]:
			var.session[0][1].write(command + "\n")
		if var.server[0] and var.server[1]:
			status = requests.post((var.server[2] + "set/com"), data={"password": var.server[3], "data": command}).text
			if status != "200":
				print("")
					print("发送命令到服务器时发生错误。")
	@event.command
	def host(command):
		print("")
		var.host = str(tools.arg("IP：", "host ", command))
		if "." not in var.host:
			print("无效的 IP。")
		print("")

	@event.command
	def port(command):
		print("")
		try:
			var.port = int(tools.arg("端口：", "port ", command))
		except Exception as ex:
			print("发生错误。", ex)
		print("")

	@event.command
	def password(command):
		print("")
		var.password = str(tools.arg("密码：", "password ", command))
		print("")

	@event.command
	def run():
		data = {"agreed": False, "commands": [""]}
		app = flask.Flask("Raven-Storm-Server")
		# app.config["DEBUG"] = True

		@app.route('/get/com<pos>', methods=["GET", "POST"])
		def command_get(pos=0):
			if request.form['password'] == var.password:
				try:
					return str(data["commands"][int(pos)])
				except Exception:
					return "500"
			else:
				return "无效的密码"

		@app.route('/get/agreed', methods=["GET", "POST"])
		def agreed_get():
			if request.form['password'] == var.password:
				return str(data["agreed"])
			else:
				return "无效的密码"

		@app.route('/set/com', methods=["GET", "POST"])
		def command_set():
			if request.form['password'] == var.password:
				data["commands"].append(request.form["data"])
				return "200"
			else:
				return "无效的密码"

		@app.route('/set/agreed', methods=["GET", "POST"])
		def agreed_set():
			if request.form['password'] == var.password:
				data["agreed"] = request.form["data"]
				return "200"
			else:
				return "无效的密码"

		@app.route('/reset', methods=["GET", "POST"])
		def reset_data():
			if request.form['password'] == var.password:
				data = {"agreed": False, "commands": [""]}
				return "200"
			else:
				return "无效的密码"

		app.run(host=var.host, port=var.port, use_reloader=False)
		var.stop()
		quit()


def setup(console):
	console.ps1 = "Server> "
	console.add(Main(console), event)

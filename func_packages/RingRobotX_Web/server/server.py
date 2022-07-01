import time
import func_packages.RingRobotX_Web.server.Websocket
import tornado.ioloop
import tornado.web
import model.config
import threading
import asyncio
import json
import func_packages.RingRobotX_ChatHistory.main
import bcrypt
import model.logger


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):

    def get(self):
        global history
        history = None
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('index.html')


class StudyHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('study.html')

class CLIHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        salt = bcrypt.gensalt(rounds=10)
        hashed = bcrypt.hashpw(model.config.fastGetConfig("RingRobotX_Web")["password"].encode(), salt)
        self.render('cli.html',token=hashed.decode(),port=str("{}").format(model.config.fastGetConfig("RingRobotX_Web")["websocket_port"]))


class DhHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('dh.html', history=func_packages.RingRobotX_ChatHistory.main.get_history())


class HistoryHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
        else:
            res = {'code': 0, 'message': 'ok', 'history': json.dumps(func_packages.RingRobotX_ChatHistory.main.get_history())}
        self.write(json.dumps(res))
        self.finish()


class GetLogHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        with open(model.logger.module_logfileMain, encoding="utf-8") as file_obj:
            contents = file_obj.readlines()
            self.render('log.html', log=contents)


class ChatHandler(BaseHandler):
    def post(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
            print('chl1..........')
        else:
            global jineng_s_r
            query = self.get_argument('query', '')
            sc_s = str(query)
            if sc_s != '':
                model.hook.runhook_fast("RRCore.Model.FuncAction",sc_s,"return")
                print('chl3..........')
            res = {'code': 0, 'message': 'ok'}
        self.write(json.dumps(res))
        self.finish()


class LoginHandler(BaseHandler):
    def get(self):

        if self.current_user:
            self.redirect('/')
            return
        '''
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name"><br/>'
                   'Password: <input type="password" name="password">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')
        '''
        self.render('login.html')

    def post(self):

        if model.config.fastGetConfig("RingRobotX_Web")["password"] == self.get_argument('password', default=''):  # 可自行修改
            self.set_secure_cookie("user", self.get_argument("name"))
            self.redirect("/")
        else:
            self.write('用户名或密码错误，请尝试重新输入')
            pass


settings = {
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "template_path": "./func_packages/RingRobotX_Web/server/template",
    "static_path": "./func_packages/RingRobotX_Web/server/static",
}


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/study", StudyHandler),
        (r"/dh", DhHandler),
        (r"/history", HistoryHandler),
        (r"/chat", ChatHandler),
        (r"/log", GetLogHandler),
        (r"/cli",CLIHandler)
    ], **settings)


app = make_app()


def start_server():
    asyncio.set_event_loop(asyncio.new_event_loop())
    app.listen(model.config.fastGetConfig("RingRobotX_Web")["listen_port"])
    tornado.ioloop.IOLoop.current().start()

def run():
    threading.Thread(target=start_server).start()
    func_packages.RingRobotX_Web.server.Websocket.run()
    model.logger.moduleLoggerMain.info("[Server] 后台启动，地址：localhost:" + str(model.config.fastGetConfig("RingRobotX_Web")["listen_port"])+"\n 密码："+model.config.fastGetConfig("RingRobotX_Web")["password"])

def hread(readlog_r):
    global readlog_s_r
    readlog_s_r = readlog_r
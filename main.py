__author__ = 'Andrey'

import os
import datetime
import json

from db import Achivement
from db import Session

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options


define("port", default=12345, help = "Check localhost:port", type = int)
application_settings = {"debug": True,
                        "static_path": os.path.join(os.path.dirname(__file__), "static"),
                       }


class HomePageHandler(tornado.web.RequestHandler):
    def get(self):
        session = Session()

        try:
            achivements = session.query(Achivement)

            self.render("templates/home.html",
                    achivements = achivements)
        except:
            raise

        session.close()


class NewAchivementPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/newAchivement.html")


class DataProvider(tornado.web.RequestHandler):
    def get(self):
        function_name = self.get_argument("f", default=None, strip=False)

        handlers = {
            'getSimpleAnswer': self.get_simple_answer,
            'insertAchivement': self.insert_achivement,
        }
        default_handler = lambda: {'result': 'not implemented'}

        handler = handlers.get(function_name, default_handler)
        self.write(handler())
        return

    def get_simple_answer(self):
        result = str(datetime.datetime.now().time().isoformat()) + " SimpleAnswer: OK!"
        json_result = json.dumps({"result": result})
        return json_result

    def insert_achivement(self):
        title = self.get_argument("title", default=None, strip=False)
        description = self.get_argument("description", default=None, strip=False)
        xtimes = self.get_argument("xtimes", default=None, strip=False)
        progress_current = self.get_argument("progress_current", default=None, strip=False)
        progress_end = self.get_argument("progress_end", default=None, strip=False)
        done = self.get_argument("progress_end", default=None, strip=False)

        newAchivement = Achivement()
        newAchivement.achivement_title = title
        newAchivement.achivement_description = description
        #newAchivement.achivement_xtimes = xtimes
        #newAchivement.achivement_progress_current = progress_current
        #newAchivement.achivement_progress_end = progress_end
        #newAchivement.achivement_done = done
        #newAchivement.achivement_description = description

        session = Session()
        try:
            session.add(newAchivement)
            session.commit()
        except:
            session.rollback()
            raise

        result = newAchivement.achivement_id

        session.close()

        json_result = json.dumps({"result": result})
        return json_result


def createTornadoApplication():
    tornado.options.parse_command_line()

    application = tornado.web.Application(
        [
            (r"/", HomePageHandler),
            (r"/DataProvider", DataProvider),
            (r"/NewAchivement/", NewAchivementPageHandler),
            (r"/NewAchivement", NewAchivementPageHandler),
        ],
        **application_settings)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


def runApplication():
    #print "Visit http://localhost:" + str(tornado.options.options.port) + "/NewAchivement/"
    print "Visit http://localhost:" + str(tornado.options.options.port)
    createTornadoApplication()


def main():
    #TODO: do close port before tornado start

    trying = True
    tornado_port = tornado.options.options.port

    while trying:
        try:
            runApplication()
            trying = False
        except:
            tornado_port = tornado_port + 1
            runApplication()
            trying = False


if __name__ == "__main__":
    main()
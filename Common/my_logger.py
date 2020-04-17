import logging


class Log(object):
    def __init__(self, name=__name__, path='mylog.log', level='DEBUG'):
        """
        :param name:自定义的日志的名字，默认是root
        :param path:
        :param level:
        """
        self.__name = name
        self.__path = path
        self.__level = level
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)

    def __ini_handler(self):
        """
        初始化handler
        :return: handler
        """
        #创建一个handler用于输出到控制台
        stream_handler = logging.StreamHandler()
        #创建一个handler用于输出到文件中
        file_handler = logging.FileHandler(self.__path, encoding='utf-8')
        return stream_handler, file_handler

    def __set_handler(self, stream_handler, file_handler, level='DEBUG'):
        """
        设置handler级别并添加到logger收集器
        :param stream_handler: 控制台的handler
        :param file_handler: 文件输出的handler
        :param level: 日志的级别
        :return: None
        """
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

    def __set_formatter(self, stream_handler, file_handler):
        """
        设置日志输出格式
        :param stream_handler: 控制台的handler
        :param file_handler: 件输出的handler
        :return: None
        """

        """
        name:logger的名字
        filename:调用日志输出的函数的模块的文件名
        lineno调用日志输出函数的语句所在的代码行
        levelname：文件形式的日志级别
        message：用户输出的信息
        """
        #设置日志输出的格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    def __close_handler(self, stream_handler, file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()

    @property
    def Logger(self):
        """构造收集器，返回looger"""
        stream_handler, file_handler = self.__ini_handler()
        self.__set_handler(stream_handler, file_handler)
        self.__set_formatter(stream_handler, file_handler)
        self.__close_handler(stream_handler, file_handler)
        return self.__logger


# if __name__ == '__main__':
#     path = r'F:\PycharmProjects\ComketangpaiAutoPytest\OutPuts\log\log2.txt'
#     log = Log(__name__, path)
#     logger = log.Logger
#     logger.debug('I am a debug message')
#     logger.info('I am a info message')
#     logger.warning('I am a warning message')
#     logger.error('I am a error message')
#     logger.critical('I am a critical message')
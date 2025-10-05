import logging

def init_logger(out_pth: str = r'E:\Test\4'):
    # 创建一个 logger 对象
    logger = logging.getLogger(__name__)
    # 设置日志的级别为 INFO，即只记录 INFO 及以上级别的日志
    logger.setLevel(logging.INFO)

    # 创建一个文件处理器，将日志信息写入指定的文件
    file_handler = logging.FileHandler(out_pth)
    file_handler.setLevel(logging.INFO)

    # 创建一个控制台处理器，将日志信息输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 定义日志的格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将文件处理器和控制台处理器添加到 logger 中
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# 以下是 logging 库常用方法的注释说明
# logger.debug(msg, *args, **kwargs)
# 记录调试级别的日志信息，用于调试程序时输出详细信息。只有当日志级别设置为 DEBUG 时才会记录。
#
# logger.info(msg, *args, **kwargs)
# 记录信息级别的日志信息，用于记录程序正常运行时的重要信息。
#
# logger.warning(msg, *args, **kwargs)
# 记录警告级别的日志信息，用于提示可能存在的问题，但程序仍可继续运行。
#
# logger.error(msg, *args, **kwargs)
# 记录错误级别的日志信息，用于记录程序运行过程中出现的错误，但不影响程序的整体运行。
#
# logger.critical(msg, *args, **kwargs)
# 记录严重错误级别的日志信息，用于记录程序运行过程中出现的严重错误，可能导致程序无法继续运行。
#
# logger.exception(msg, *args, exc_info=True, **kwargs)
# 记录异常级别的日志信息，用于记录程序运行过程中出现的异常，并输出异常的堆栈信息。
# 通常在捕获异常时使用，例如：
# try:
#     # 可能会抛出异常的代码
#     result = 1 / 0
# except ZeroDivisionError:
#     logger.exception("发生了除零错误")

# 以下是使用示例
if __name__ == "__main__":
    logger = init_logger('example.log')
    logger.info("这是一条信息级别的日志")
    logger.warning("这是一条警告级别的日志")
    logger.error("这是一条错误级别的日志")
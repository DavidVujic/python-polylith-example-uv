from example import greeting, log

logger = log.get_logger("The DEV logger")
data = greeting.hello_world()

logger.info(data)

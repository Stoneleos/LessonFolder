import logging
import colorlog

# Настройка цветного логирования
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(name)s:%(message)s'
))

logger = colorlog.getLogger('example')
logger.addHandler(handler)
logger.setLevel(logging.ERROR)
logger.propagate = False  # Отключаем передачу в родительский логгер


# Теперь логи будут цветными
logger.debug("Подробная информация для отладки")      # СЕРЫЙ
logger.info("Общая информация о работе")              # БЕЛЫЙ  
logger.warning("Предупреждение о проблеме")           # ЖЕЛТЫЙ
logger.error("Ошибка в программе")                    # КРАСНЫЙ

# если не удалось подключиться к базе данных
try:
    # код подключения к базе данных
    pass
except:
    logger.critical("Критическая ошибка!")     
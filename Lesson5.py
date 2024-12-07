import colorama
import inspect
import requests

colorama.init()

print(colorama.Fore.RED + "Text" + colorama.Style.RESET_ALL)
print(colorama.Back.GREEN + "Background" + colorama.Style.RESET_ALL)

print(hasattr(colorama, 'init'))
print(type(colorama.Fore))
print(callable(getattr(requests, 'get', None)))
print(inspect.isfunction(inspect.signature))

#Это вроде должно быть правильно, уже в гугле и чатгпт посмотрел, но мой компьютер почему то выдаёт ошибку того, что у меня
#tempfile отсутствует
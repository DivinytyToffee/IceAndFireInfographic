Небольшая программа для получения данных, обработки и визуализации с www.anapioficeandfire.com, где доступно api 
по миру Песни Льда и Пламени.

## Использование
Установить пакеты из requirements.txt

Запустить файл main.py.

После первого запуска создаться 3 json файла с данными, от куда их можно будет после подгружать без постоянного 
обращения к внешнему api.
Плюс папка images, куда сохраняются графики.

Для того что бы запрашивать данные из json файлов надо в файле main у вызова `cl.run` поменять флаг 
`load_from_json` с `False` на `True` 
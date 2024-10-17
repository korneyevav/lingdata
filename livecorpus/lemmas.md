Импортируем из elan нужный слой words, убираем галочку с длительности и с сс.мс в формате времени

.*\t на ничто
Копируем и вставляем в mystem
Выдачу mystem вставляем в файл
.+{([а-яА-ЯЁё-]*)=(.*)} на \1\n\2
(\n[?!/:;,-]) на \1\n
.+{(.+)} на \1\n
Вставляем результат в переменную mystem в коде

Импортируем из elan нужный слой words опять
\t[А-Яа-яЁё/.?=!A-Za-z-]*?\n на \n
words(.*) на lemma\1\nmorph\1
Вставляем результат в переменную timecodesetc в коде, стираем лишний \n в конце при необходимости

Код в файле lemmatise.py

Запускаем код
Находим файл elanimport.txt, перекодируем его в UTF-8
Импортируем в ELAN, ставим таб как разделитель, выставляем значения колонок
Все
Можно и проще немного, наверное, например, сделать автоматическую выдачу mystem через API, если оно есть, и регулярки сделать тоже через python, но я в этом не разбираюсь, а работает и так, плюс вручную надо делать не так много, и так несколько даже удобнее для отладки
Надеюсь не большая проблема, что у меня немного другой формат выдачи файла - не сначала все леммы, потом вся морфология, а для каждого слова сначала одно, потом другое. Импортируется нормально, так что, наверное, это не проблема
Еще, надеюсь, не проблема, что одно отдельное английское слово не стал отдельно закидывать в mystem, вряд ли это очень важно; хотя можно сделать и вручную при желании

Есть несколько случаев омонимии ("свете" посчиталось как форма от "Света", а не "свет"; "эм" не как междометие, а как существительное -- в целом с междометиями есть проблемы, они не всегда нужным образом размечены), что показывает, что отсутствие учитывания синтаксических связей слова иногда мешает правильному определению его морфологии. Также, очевидно, не учитывался смысл, что иногда важно -- например, "там". Есть спорные случаи, например, учет "дома" как наречия, а не словоформы от "дом", однако это не задача морфологического анализатора, это больше теоретический вопрос. В целом же морфологический анализатор справился довольно неплохо, за исключением указанных случаев ошибки редки. Эти же случаи во многом обусловлены особенностями устной речи (междометия, "там", неправильная разметка незаконченных слов), однако не только -- выше написано о синтаксисе и семантике.
import random

from pymorphy2 import MorphAnalyzer
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import re
import nltk

a1 = ['Здравствуйте Мне нужно оформить бронь номера', 'Подскажите список услуг которые вы предоставляете',
      'какие допуслуги вы предоставляете', 'какие допуслуги предоставляются в гостинице',
      'привет, что еще может ваш отель предоставить', 'хочу у вас снять комнату', 'у вас есть бар в гостинице',
      'Здравствуйте где я смогу оставить машину', 'Здравствуйте мне нужен номер в гостинице одноместный',
      'Доброго дня Расскажите о дополнительных услугах предоставляемых гостиницей', 'Во сколько нужно выехать',
      'скажите время заезда в номер', 'Есть парковочные места возле отеля',
      'Доброго дня пожалуйста уточните время заселения и выселения', 'Что предоставляет гостиница',
      'В какое время освободиться номер', 'Какая то стоянка имеется у вас', 'Какими номерами вы располагаете',
      'Добрый день Какое время заезда ',
      'Скажите пожалуйстакакими доп  услугами можно воспользоваться в вашей гостинице',
      'Сколько стоит у вас поставить автомобиль на стоянку',
      'Здравствуйте скажите смогу ли я оставить автомобиль на стоянку возле гостиницы ',
      'Здравствуйте Скажите когда можно будет заселиться в номер', 'В какое время я могу заселиться в номер',
      'Какое время заезда и выезда в номер', 'Во сколько мы можем войти в комнату',
      'В какое время можно заехать в номер', 'Какими ещё услугами я могу воспользоваться в гостинице',
      'скажите пожалуйста время заселения в номер', 'во сколько заезд', 'когда заезд',
      'Не могли бы вы сказать мне сколько у вас комнат', 'При отеле есть парковочные места',
      'Во сколько нужно заехать в номер', 'Привет Расскажи о доп услугах в этой гостинице',
      'Добрый день Скажите стоимость суточной парковки у отеля', 'Какое точное время заселения в гостиницу',
      'в какое время можно заселиться', 'какого числа можно будет заселиться', 'Я хочу сменить комнату',
      'Сколько времени заемет время до номера', 'как долго я могу оставаться в комнате', 'Во сколько заезд в номер',
      'В какое время я смогу заселиться', 'Здравствуйте я хочу снять комнату',
      'Привет во сколько мне зарегистрироваться', 'Когда я могу заселиться',
      'Скажите пожалуйста какими ещё услугами гостиницы я могу воспользоваться',
      'В котором часу нужно освободить номер', 'Здравствуйте долго бронировать по времени номер в отеле ',
      'Здравствуйте не подскажете где можно припарковаться у вашего отеля', 'Включён ли завтрак в проживание',
      'Оформите мне бронь номера', 'Когда можно заехать', 'Расскажите о доступных номерах',
      'Здравствуйте можно фото двухместного номера', 'позвольте зарезервировать комнату у вас',
      'у вас до 12 часов время заезда', 'здравствуйте входит ли в услуги гостиницы завтрак и обед',
      'хочу получить информацию о номерном фонде', 'добрый день в вашей гостинице есть спец предложение',
      'я хотела бы узнать когда я могу заселиться в мой номер',
      'здравствуйте мне нужен номер на двоих человек на 17 мая хочу забронировать заранее может подсказать мне сумму на бронь номера заранее спасибо',
      'во сколько заселяют и выселяют из номеров', 'заезд выезд', 'что дополнительно вы можете предложить',
      'хай что есть дополнительного в гостинице', 'как долго я могу войти в комнату ночью',
      'доброе утро я могу где нибудь припарковаться у вашего отеля',
      'здравствуйте какие развлекательные программы вы можете предложить', 'когда вы будете заезжать',
      'здравствуйте можете уточнить ц вас есть стоянка при отеле', 'есть в наличии парковка сколько она стоит',
      'наличие парковки', 'во сколько можно заехать в номер', 'подскажите можно у вашего отеля оставить авто',
      'добрый день можно ли ознакомиться со всеми услугами вашей гостиницы', 'когда я могу заехать в номер',
      'добрый день мне нужно место в вашей гостиной',
      'здравствуйте интересует такой вопрос какие есть номера в вашей гостинице заранее спасибо за ответ',
      'добрый день сколько стоит парковка', 'добрый день какими еще услугами можно воспользоваться в гостинице',
      'во сколько заезжаем', 'когда время заселения в номер', 'на данный момент гостиница работает',
      'в какой день заезд', 'сколько будет стоит стоянка', 'категории номеров в отеле какие представлены',
      'подскажите во сколько можно заселиться в номер',
      'добрый день будьте добры подскажите пожалуйста какими дополнительными услугами я могу воспользоваться в вашей гостинице трансфер аквапарк пребывание с животными',
      'добрый день подскажите в какое время я могу заселиться в номер',
      'есть ли фиксированное время заселения и выселения',
      'добрый день в стоимость моего проживания будет включен завтрак',
      'доброго времени суток подскажите что входит в оплату за номер в вашей гостинице',
      'добрый день скажите пожалуйста в какое время мы можем заселится', 'время выселения из номера',
      'доброго времени суток какие еще слуги предоставляет данная гостиница', 'добрый день у нас номер 345',
      'скажите какой у вас выбор номеров есть люксы синглы номера на двоих',
      'здравствуйте в какое время происходит заселение в номер', 'здравствуйте подскажите время заезда в номер',
      'добрый день какими дополнительными услугами я могу воспользоваться в вашей гостинице',
      'доброе время суток хотелось бы узнать можно ли припарковаться возле отеля',
      'здравствуйте сколько стоит парковка при отели', 'пожалуйста дайте мне знать если у вас есть номер 345',
      'в какое время можно заедать в номер', 'во сколько можно заезжать в отель', 'скажите время заселения и выезда',
      'могу я узнать о номерах', 'какие имеет значение на какое время заезда номер', 'когда заезжаем в номер',
      'здравствуйте каким образом я могу заказать у вас проживание в хотеле', 'во сколько заселение в номер',
      'в какое время номер будет готов к заселениею', 'что еще есть в гостинице спа салон ресторан',
      'когда заселятся по времени в номер', 'подскажите пожалуйста время когда заселения и выселения',
      'нужно ли платить за парковку', 'к 6 которому времени необходимо заехать в номер',
      'мое время заезда в номер 22 00', 'во сколько обед в отеле',
      'сообщите пожалуйста в какое время я могу заселиться в номер', 'у нас лучшие номера',
      'добрый день подскажите пожалуйста какими еще услугами я могу воспользоваться в вашей гостинице',
      'у вас есть где припарковаться', 'скажите пожалуйста сколько там комнат',
      'добрый день есть ли свободные места для парковки автомобиля в ночное время суток',
      'здравствуйте подскажите пожалуйста стоимость стоянки и с какой стороны здания она находится',
      'когда можно заселиться', 'категории свободных номеров', 'привет я хочу поселиться у вас как мне это сделать',
      'подскажите пожалуйста время бронирвоания', 'в какое время я могу заехать в номер',
      'добрый день подскажите пожалуйста в котором часу я могу въехать в номер и до которого часа мне необходимо номер покинуть',
      'хочу бронь оформить', 'пожалуйста скажи мне номер который у тебя есть',
      'добрый день нужна бронь свободного номера', 'какой фонд вас интересует',
      'в какое время нужно заехать в гостиницу', 'когда я могу заселиться в номер', 'время заседания и выселения',
      'день добрый если у нас парковку у отеля и сколько она стоит', 'что вы можете предложить мне дополнительно',
      'здравствуйте в вашей гостинице имеется спа', 'во сколько у вас проходит заселение',
      'здраствуйте у вас есть автомобильная стоянка и сколько стоит', 'в 11 можно заехать в номер',
      'во сколько можно заехать в гостиницу', 'хочу узнать какое точное время заселения в номер',
      'сколько стоит машина', 'в котором часу заезд в номер', 'чем можно заняться в отеле',
      'подскажите пожалуйста сколько у вас номерной фонд', 'когда и во сколько заежать в номер',
      'здравствуйте подскажите пожалуйста количество двухместных номеров', 'расскажите какими номерами вы распологаете',
      'в какое время я могу заселиться', 'когда происходит заселение и выселение',
      'доброго времени суток можно познакомиться с перечнем всех возможностей организации',
      'подскажите в какое время можно заехать в снятый номер', 'доброе нет у нас нету мест в отеле',
      'мне нужен двухместный номер на 2 июня есть свободные', 'какое время выселения из номера',
      'добрый вечер сообщите перечень услуг вашего отеля пожалуйста',
      'привет мне очень нужны номера которые вы мне дадите я знаю что это поможет мне ты хороший человек',
      'день добрый я хочу поставить бронь', 'перечень дополнительных услуг предоставляемых гостиницей',
      'здравствуйте а не подскажете есть ли тут автомобильная стоянка если есть то сколько стоит',
      'во сколько можно въехать в номер', 'каково время выезда из номера',
      'скажите пожалуйста сколько у вас всего номеров', 'сколько у вас есть номеров и какого они типа',
      'во сколько можно въезжать в номер', 'с какого времени я могу заселиться', 'когда chek in',
      'у меня нет номер фонда', 'где лучше отдохнуть', 'время заселения и выезда', 'сколько стоит двухместный номер',
      'привет уточните пожалуйста наличие и стоимость автомобильной стоянки возле гостиницы',
      'какова стоимость автостоянки', 'есть ли около гостиницы автомобильная стоянка и стоимость',
      'здравствуйте смогу ли я припарковаться возле отеля', 'я хочу знать о вашей парковке',
      'во сколько уже можно заселяться в номере', 'сколько осталось у вас номеров в отеле',
      'когда можно будет приехать в гостиницу', 'время заселения в номер',
      'здравствуйте расскажите подробнее об услугах предоставляемых гостиницей',
      'здравствуйте сколько стоит проживание', 'когда можно будет заселиться',
      'здравствуйте можете рассказать подробнее об услугах предоставляемых гостиницей',
      'добрый день скажите пожалуйста во сколько нужно приехать чтобы пошла оплата номера и во сколько нужно выезжать чтобы не переплатить за лишние сутки',
      'когда случился заезд', 'время прибытия в номер', 'имеютс ли у ва номера пожалуйста подскажи',
      'сколько номеров я могу забронировать сейчас', 'в номер во сколько заезжать', 'если ли кондиционер в номере',
      'здравствуйте подскажите пожалуйста что входит в перечень дополнительных услуг в вашей гостинице',
      'добрый день я хочу забронировать номер на троих с раздельными кроватями',
      'здравствуйте действует ли бронь на завтрашний день', 'есть ли в вашем отеле good morning парковочное место',
      'день добрый меня интересует информация о видах номеров в вашей гостинице', 'какая тематика должна быть',
      'когда будет заезд и выезд', 'могу ли я получить информацию об имеющихся у вас номерах',
      'когда могу заселится в номер', 'в какой часовой пояс я могу заселиться в отель',
      'подскажите чек ин и чек аут в отеле', 'хорошего дня не могли бы вы рассказать когда будет ланч',
      'в котором часу ожидать заезд в номер', 'расскажите о дополнительных услугах гостинницы',
      'добрый день есть ли возможность заказать номер для семейной пары с дополнительной комнатой',
      'когда можно заехать в номер', 'здравствуйте можете помочь зарегестрировать номер у вас',
      'здравствуйте хотелось бы узнать у вас имеется автомобильная стоянка не подскажите стоимость данной услуги',
      'я плохо иметь парковку у отеля', 'привет бронь в отеле',
      'какова стоимость и комфортабельность свободных номеров',
      'сколько стоит свободный номер и на сколько человек он предусмотрен', 'когда можно будет заехать',
      'добрый день модео ли приехать к вам в отель на своем автомобиле', 'когда заселяться', 'лучший номер бронь',
      'что еще я могу получить у вас', 'заезд в какое время в номер',
      'меня интересует есть ли в вашем отеле парковочные места', 'бронирование номеров вызов такси',
      'какое время заезда в номер у нас', 'сауна бассейн баня фитнес зал предоставляет гостиница',
      'доброго времени суток забронируйте мне номер в отеле пожалуйста', 'сколько свободных номеров в вашей гостинице']

a2 = ['Перечислите доступные услуги отеля', 'Добрый день Подскажите, какие услуги доступны в вашем отеле',
      'Перечислите доступные услуги отеля', 'расскажите про дополнительные услуги', 'дополнительные услуги',
      'Добрый день Какие в гостинице есть дополнительные услуги', 'Какие ещё услуги может мне предоставить гостиница',
      'Добрый день Есть ли в гостинице дополнительные опции',
      'Здравствуйте какие дополнительные услуги предоставляют гостиницы',
      'Добрый день Есть ли какиенибудь дополнительные услуги',
      ' ваша гостиница Какие дополнительные услуги предоставляет', 'какие есть услуги в гостинице',
      'Здравствуйте какие услуги предлагает отель', 'Здравствуйте у вас есть другие услуги',
      'Какие дополнительные услуги вы предоставляете', 'Какие в ностинице бесплатные услуги',
      'какие услуги еще имеються у вашей гостинице', 'добрый день подскажите какие у вас есть доп услуги',
      'добрый день расскажите пожалуйста какие дополнительные услуги присутствуют в вашей гостинице',
      'добрый день у вас в гостинице есть дополнительные услуги',
      'добрый день есть ли дополнительные услуги в гостинице', 'добрый день какие есть дополнительные услуги у отеля',
      'здравствуйте подскажите пожалуйста есть ли в гостинице дополнительные услуги',
      'подскажите пожалуйста какие еще услуги предоставляет ваша гостиница',
      'добрый день в вашей гостинице есть дополнительные услуги',
      'добрый день подскажите какие услуги дополнительно предоставляет отель', 'какие услуги гостинице есть дополнение',
      'добрый день уточните пожалуйста предоставляет ли ваша гостиница вспомогательные услуги для клиентов',
      'здравствуйте а есть дополнительные услуги какие', 'каковы дополнительные услуги предоставляемые гостиницей',
      'могу ли я получить какие то дополнительные услуги в гостинице',
      'добрый день подскажите пожалуйста ваша гостиница предоставляет какие то дополнительные услуги',
      'какие еще услуги можно заказать в гостинице', 'есть ли в гостинице не стандартные услуги',
      'какие услуги у вас есть', 'какие есть доп услуги',
      'добрый день есть ли в гостинице какие нибудь дополнительные услуги', 'хочу узнать какие есть услуги в гостинице',
      'добрый день гостиница предоставляет какие либо дополнительные услуги если да то какие',
      'привет подскажите какие у гостиницы есть дополнительные услуги',
      'здравствуйте я хотел бы знать какие услуги предлагаются в отеле',
      'предоставляет ли гостиница дополнительные услуги',
      'добрый день что входит в дополнительные услуги вашей гостиницы',
      'добрый день подскажите в гостинице есть трансфер',
      'добрый день подскажите пожалуйста какие услуги есть в вашем отеле',
      'какие дополнительные услуги предоставляет гостиница',
      'могу ли я узнать а какие дополнительные услуги предоставляет гостиница',
      'зравствуйте какие услуги может предложить гостиница', 'какие услуги предоставляет гостиница',
      'добрый день гостиница предоставляет дополнительные услуги', 'какие услуги выполняет гостиница',
      'а какие у вас услуги']

a3 = ['приветствую подскажите есть ли у вас автомобильная парковка',
      'Здравствуйте Уточните можно ли оставить машину на территории', 'Здравствуйте у вас есть парковка для машины',
      'Здравствуйте Скажите пожалуйста смогу ли я припарковаться на территории отеля',
      'Здравствуйте у вас есть парковка на территории и сколько в час', 'Здравствуйте В отеле есть парковка',
      'Здравствуйте у вас есть парковка на территории отеля Какие условия',
      'Здравствуйте Подскажите мне можно ли припарковаться на территории отеля ',
      'Скажите Пожалуйста у имеются свободные парковки на территории отеля',
      'Здравствуйте На территории отеля есть парковка', 'Черт у вас есть парковка и какова цена',
      'Здравствуйте на территории есть парковка', 'Здраствуйте на территории отеля у вас есть летние веранды',
      'Здравствуйте а у вас есть автостоянка',
      'здравствуйте подскажите пожалуйста на территории отеля есть место для стоянки автомобиля',
      'здравствуйте у вас есть бронь', 'здравствуйте меня интересует есть ли у вас парковка на территории отеля',
      'скажите пожалуйста есть ли у вас услуги для проживания с домашними животными',
      'добрый день мне нужна парковка на территории отеля есть ли такая услуга',
      'здравствуйте есть ли у вас парковка рядом с гостиницей если есть какая стоимость парковки в час',
      'добрый день есть место для парковки автомобиля и какая цена на сутки',
      'здравствуйте у вас есть бесплатная парковка в отеле', 'доброе утро у вас есть платная парковка',
      'на территории отеля имеется парковка', 'здравствуйте у вас имеется парковка при гостинице',
      'у отеля есть своя парковка', 'парковка бесплатная', 'имеется ли у вас парковка',
      'доброе утро есть ли на территории отеля парковка',
      'здравствуйте имеется ли парковка при гостинице и входит ли ее стоимость в проживание',
      'здравствуйте рядом с вами есть парковка', 'добрый вечер подскажите пожалуйста есть ли у вас стоянка для авто',
      'здравствуйте меня интересует есть ли у вашего отеля автомобильная парковка',
      'добрый день в вашем отеле есть своя парковка',
      'здравствуйте я хотела бы узнать могу ли я припарковать авто на территории вашего отеля',
      'здравствуйте есть ли место для автомобиля на территории вашего заведения',
      'у меня нет парковки на территории отеля',
      'здравствуйте скажите пожалуйста есть ли парковка на территории отеля и какая стоимость',
      'добрый вечер у вас есть парковка и какая стоимость', 'имеится ли у вас парковка',
      'добрый день я хотела бы узнать при вашем офисе есть парковка для автомобилей и какая стоимость в час',
      'хотел бы узнать на счет парковки на территории отеля', 'пожалуйста у вас есть парковка',
      'добрый вечер подскажите пожалуйста есть ли автомобильная стоянка на территории и какова ее стоимость',
      'добрый день подскажите на территории отеля имеется парковка и какова ее стоимость',
      'здраствуйте у вас есть парковка', 'добрый день у вас есть парковка на территории отеля',
      'здравствуйте а у вас есть стоянка для авто', 'доброе утро скажите есть ли у вас бесплатная охраняемая стояка',
      'здравствуйте подскажите пожалуйста на территории отеля есть ли парковка',
      'здравствуйте есть ли у вас парковка для гостей',
      'здравствуйте подскажите пожалуйста а на территории вашего отеля есть автомобильная парковка',
      'здравствуйте какова стоимость парковки на территории отеля', 'привет в отеле есть парковка для гостей',
      'здравствуйт подскажите пожалуйста есть ли у вас парковка для персонального авто',
      'здравствуйте мы приедем на своем автомобиле подскажите пожалуйста можно будет припарковать машину на территории гостиницы',
      'добрый день у вас на территории можно поставить авто на парковку на время отдыха',
      'добрый день возможно ли припарковать авто на территории вашего отеля',
      'добрый день подскажите есть ли у вас на территории гостиницы парковка платная или бесплатная',
      'доброе утро у вас есть парковка на территории отеля', 'привет пожалуйста на этом сайте есть парковка',
      'здравствуйте подскажите пожалуйста есть ли возможность поставить машину рядом',
      'есть ли парковка на территории отеля', 'у вас есть свободные места на парковке',
      'доброе утро парковка в отеле имеется', 'у вас есть парковка', 'доброе утро у вас есть парковка',
      'здравствуйте есть ли возможность припарковаться на территории отеля',
      'скажите есть ли парковка на территории отеля', 'есть парковка на территории отеля']

a4 = ['хочу у вас снять номер', 'Здравствуйте Есть ли возможность забронировать номер в вашем отеле',
      'Доброе утро я хотел бы забронировать номер в вашем отеле',
      'Здравствуйте Мне нужно забронировать номер в вашем отеле на следющий месяц',
      'Здравствуйте я хотел бы забронировать номер в вашем отеле', 'Привет Как я могу забронировать в гостинице номер',
      'Как забронировать номер в вашем отеле', 'Здравствуйте Давайте забронируем номер люкс в вашем отеле',
      'Номер в отеле', 'Добрый день у вас есть свободные номера в вашем отеле Я хочу забронировать номер',
      'Можно ли забронировать номер в вашем отеле', 'День добрый Я хотел бы зарезервировать номер в вашем отеле',
      'я хочу забронировать отель', 'Я хочу забронировать номер',
      'Здравствуйте я хочу забронировать номер в вашем отеле на этот вечер',
      'Здравствуйте Могу ли я забронировать номер в вашем отеле', 'Здравствуйте можно забронировать номер в отеле',
      'привет мне нужен номер в отеле', 'здравствуйте я хочу забронировать номер в отеле',
      'здравствуйте могу ли я у вас забронировать номер', 'здравствуйте могу я забронировать номер',
      'здравствуйте я хотел бы забронировать номер в отеле', 'здравствуйте можно ли забронировать номер',
      'здравствуйте нужен номер в вашем отеле', 'привет мне нужно место в вашем отеле',
      'здравствуйте как забронировать номер в отеле', 'здравствуйте мне бы заказать номер у вас в отеле',
      'здравствуйте могу ли я забронировать номер в вашей гостинице',
      'добрый день хотелось бы забронировать двухместный номер в вашем отеле',
      'я хочу забронировать номер в вашем отеле', 'можно забронировать у вас номер',
      'здравствуйте мне нужен номер в отеле хилтон ленинградская',
      'добрый день помогите забронировать в вашем отеле номер', 'возможно ли забронировать номер',
      'бронь в вашем отеле', 'добрый день можно у вас забронировать номер',
      'здравствуйте я могу забронировать номер в вашей гостинице',
      'здравствуйте я бы хотела осуществить бронирование номера в вашем отеле', 'здравствуйте как заказать номер',
      'здравствуйте помогите мне забронировать у вас номер', 'здравствуйте можно ли в вашем отеле забронировать номер',
      'здравствуйте мне необходимо забронировать номер на три персоны в вашем отеле',
      'я хочу забронировать номер в отеле', 'могу я забронировать у вас номер',
      'здравствуйте что нужно чтобы забронировать у вас номер', 'привет я хочу заказать номер в отеле',
      'здраствуйте мне нужно забронировать в отеле номер', 'добрый день хочу оформить бронь в вашем отеле',
      'здравствуйте у вас присутствует свободный номер в вашем отеле',
      'здравствуйте хочу зарезервировать номер в вашем отеле', 'здраствуйте как забронировать у вас номер в отеле',
      'здравствуйте мне нужно забронировать апартаменты у вас в отеле как я смогу это сделать',
      'забронировать номер в отеле', 'здравствуйте я бы хотела забронировать у вас номер',
      'хочу сделать бронь в вашем отеле', 'я хочу заказать номер в у вас в отеле',
      'здравствуйте можно забронировать номер в вашем отеле', 'мне бы хотелось забронировать номер у вас в отеле',
      'здравствуйте возможна ли бронь в вашем отеле', 'привет хочу забронировать номер',
      'здравствуйте хочу снять номер в отеле', 'добрый день могу я забронировать номер в отеле',
      'добрый вечер мне нужно забронировать номер в вашем отеле', 'могу я забронировать номер у вас',
      'здравствуйте могу ли я забронировать номер в этом отеле',
      'здравствуйте мне необходимо забронировать номер в вашем отеле']

a5 = ['Привет имеются ли у вас трехместные номера', 'а какие номера есть', 'какие у вас номера',
      'Добрый день Расскажите про номера которые есть в вашем отеле', 'у вас есть доступные номера хочу забронировать',
      'у вас есть номер люкс', 'Привет имеются ли у вас трехместные номера', 'есть ли у вас номера',
      'у вас есть двухместные номера', 'Здравствуйте скажите пожалуйста какие номера есть в отеле',
      'Какие номера в наличии', 'какие номера есть в наличии', 'Какие у вас есть виды номеров',
      'Подскажите а у вас есть номера категории стандарт', 'Подскажите пожалуйста есть ли у вас номера',
      'Здравствуйте подскажите пожалуйста как номера в гостинице свободны на 1 июня Интересуют номера люкс',
      'расскажите какие есть номера', 'У вас есть номера с видом на море', 'Расскажите про номера',
      'Добрый денькакие у вас имеются гостиничные номера',
      'Здравствуйте у вас есть свободные номера хотим забронировать', 'Скажите какие у вас номера',
      'Какие номера можете дать', 'Подскажите пожалуйста какие номера вы можете предложить мне ',
      'Какие номера доступны для бронирования', 'Здравствуйте какие сейчас номера у вас есть',
      'скажите пожалуйста есть ли у вас двух местные номера',
      'подскажите пожалуйста какие у вас имеются номера в гостиницу', 'скажите у вас есть двух местные номера',
      'добрый день есть ли у вас номера класса люкс', 'какие у вас имеются номера', 'какие есть номера',
      'у вас какие номера в налиии', 'скольки местные номера есть', 'могу ли я уточнить какие номера имеются в наличии',
      'здравствуйте хотел бы узнать какие есть номера в наличии', 'у вас есть номера люкс',
      'скажите номера какие имеются', 'добрый день хочу узнать какие номера предоставляются в гостинице',
      'подскажите пожалуйста какие у вас номера', 'подскажите пожалуйста все имеющиеся номера',
      'подскажите пожалуста есть вас люкс', 'у вас есть одноместные номера', 'добрый день расскажите про ваши номера',
      'добрый день какие номера у вас есть в наличии', 'здравствуйте у вас есть свободные номера я хочу снять один',
      'имеются ли у вас номера бизнес класса', 'подскажите пожалуйста номера у вас есть', 'у меня нет номера',
      'добрый день хотелось бы узнать какие номера представлены в вашей гостинице',
      'подскажите есть ли одноместные номера', 'напомните какие номера есть', 'какие номера у вас имеются',
      'здравствуйте скажите у вас есть свободные номера пожалуйста забронируйте для меня номер',
      'здравствуй есть свободные номера', 'у вас есть двухместные или трехместные номера',
      'какие номера можно снять в вашем отеле', 'у вас есть двухместные номера с завтраком',
      'какие есть гостиничные номера', 'добрый день какие номера сейчас свободны',
      'скажите какие в наличии есть номера', 'какие у вас номера есть', 'здравствуйте у вас есть свободные номера',
      'могу ли я узнать какие имеются у вас номера', 'хотела бы уточнить какие номера у вас есть',
      'а какие есть номера у вас',
      'какие у вас имеются номера в городе интересует трехместный номер люкс с кондеем джакузи и вай фай обязательно',
      'здравствуйте есть ли у вас свободные номера мне бы хотелось забронировать один', 'покажи номера',
      'огласить все номера в наличии можете', 'какие у вас есть номера',
      'здравствуйте подскажите пожалуйста есть ли у вас свободные номера и какая стоимость']

dataset = a1 + a2 + a3 + a4 + a5
random.shuffle(dataset)
print(dataset)

dataset = pd.DataFrame([
    dataset,
    [random.randint(0, 100) for _ in range(len(dataset))],
    [random.randint(0, 100) for _ in range(len(dataset))],
    [random.randint(0, 100) for _ in range(len(dataset))],
], columns=['query', 'col1', 'col2', 'col3'])

dataset.to_csv('data.csv')
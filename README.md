# zelen-game
Реализация игры "Зелень"

### Карты
[Все карты](https://66dd6fe7aa07a9cd796f1087--aesthetic-moxie-807fe3.netlify.app/)

* базовые карты:
  * карты рынка - 5 карт с изображением овощей (Помидор, Баклажан, Брокколи, Морковь, Кукуруза).
  * карты цены - карты, на которых лежат карты рынка; отображают текущую стоимость данного товара. 
  * карты овощей - рызыгрываются в каждом раунде по количеству игроков +1; игроки выбирают по одной карте и кладут их перед собой лицевой стороной вниз; оставшаяся карта определяет повышение цены (по изображённым на ней овощам).
  
* особые карты:
  * "Тайфунчик" - в этом раунде не будет обрушения. Все карты овощей, которые дошли до самого высшего деления и должны перескочить на низшее, остаются на высшем делении.
  * "Солнышко" - добавьте ещё одну карту овощей в дополнение к обычному ряду. В этом раунде 2 последние карты меняют цену овощей на рынке.
### Комплектность
Игра состоит из 60 карт:
 * карты рынка - 5 шт.
 * карты цены - 5 шт.
 * карты овощей - 48 шт.
 * особые карты - 2 шт.
### Раздача

 * 2-6 игроков.
 * По умолчанию задействованы все овощи, если игроков 2-3, выбирается любой овощ, из колоды убираются все карты с его упоминанием.
 * Перед игроками выкладываются 5 (или 4) основных карт овощей, каждый из которых имеет свою цену от 0 до 4 (максимальная стоимость 5). Эти карты показывают стоимость данных овощей.
 * В начале каждого раунда перед игроками выкладывается количество карт, равное количеству игроков + 1. На этих картах будет изображено три овоща (разные или одинаковые).
 * В свой ход игроки по очереди берут по одной карте (взять карту бесплатно). Оставшаяся карта определяет изменение цены на рынке.
 * Игра длится 6 раундов.

### Условие победы

У игрока самое большое количество очков. Если в конце игры количество очков у нескольких игроков одинаковое, они делят победу.

### Подсчёт очков 

Умножается количество символов овоща на его финальную цену на рынке, далее всё суммируется. 

## Пример текстового интерфейса игры

Играют Bob и Leo

```
Market: tom = 0, carr = 1, corn = 2, broc = 3
Table: / t1.ca2 /  co2.b1 / b1.ca2 /
Bob: введите, какую карту будем тянуть: t1.ca2
Bob: draw t1.ca2
Leo: введите, какую карту будем тянуть: co2.b1
Leo: draw co2.b1
Extra card: b1.ca2
-----
Market: tom = 0, carr = 3, corn = 2, broc = 4
Table: / ca2.b1 / t3 / co1.t2 /
Leo: co1.t2
Bob: ca2.b1
Extra: t3
-----
Market: tom = 3, carr = 3, corn = 2, broc = 4
Table: / b2.co1 / ca1.co2 / co3 /
Bob: ca1.co2
Leo: co3
Extra: b2.ca1
----
Market: tom = 3, carr = 4, corn = 2, broc = 1
......
-----
Market: tom = 1, carr = 4, corn = 4, broc = 3
-----
Leo WIN!!!
```


## Формат save-файла






















































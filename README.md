# scissors

Задача "камень-ножницы-бумага"

## Описание

Два игрока одновременно выкидывают одну из фигур: камень, ножницы или бумагу, не зная (не видя) результата оппонента. 
После этого оба игрока показывают свои фигуры и выявляется победитель (то есть каждому игроку известен ход оппонента 
после присуждения победы или выявления ничьей).

Один из игроков, назовем его Рандом,- компьютер, он делает ход всегда случайно (с помощью псевдослучайного ГСЧ, 
встроенного в язык).

Вопрос звучит так: Возможно ли написать алгоритм, который будет обыгрывать Рандом?

## Что в коде

Три алгоритма 

`AlgoRock` - кидает всегда только камень.

`AlgoFirst` - делает ход на основе предыдущего хода противника. Логика какая - если противник выкинул камень, то следующий
 его ход не должен быть таким же, как и предыдущий, и он выкинет бумагу или ножницы. В таком случае (пара пред. ход - наш 
 ход): К - Н, Н - Б, Б - К, чтобы или выиграть, или сыграть вничью. Первый ход делается рандомно.
 
`AlgoSecond` - разновидность первого алгоритма, только противоход делается, если противник два раза подряд выкинул одну 
 и ту же фигуру, первый ход - рандом. Если противник сменил фигуру - также рандом.
 
Также можно придумать более "умный" алгоритм, который будет делать противоход, если противник кинул подряд одну и ту же
  фигуру N раз (N > 2).

Все алгоритмы сражаются с Рандомом, так как ясно, что `AlgoFirst` и `AlgoSecond` проиграют на дистанции `AlgoRock`, так 
как они нацелены на условие, что противник будет меньше совершать ходы с повторяющейся серией, а `AlgoRock` только это и
 делает.

## Результаты

???
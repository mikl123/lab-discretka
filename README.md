# lab-discretka
Lab 2
I have create FSM for my day generation in FSM.py.

# To run program
1) Put the following code in the end FSM.py file.

`tree=FSM()
tree.send()`

2) Run the code
 
This will run cycle that will generate day timetable for 24 hours.

All states:
1) Slepping
2) Resting
3) Studying
4) Walking
5) Eating
6) Talking
7) Washing
8) Watching film
9) Shopping
10) Talking parents
11) Writting essay
Firstly the program will run base state "Sleeping"
![Диаграмма без названия drawio (1)](https://github.com/mikl123/lab-discretka/assets/69431189/3ff67c81-3e5c-42da-9470-7a00d5694229)
Key moment:
1) Always starts from "Slepping" state and change state if and only if hour=7.
2) Also different current states randomly can make state change on other.
3) After every hour, hungry+=19, so when in is more than 80, state is changed on eating where hungry is setted on 0.
4) If study after hour>=20 then get annoyed and change state on "Writing essay"
5) if hour=23 then set state on "Slepping".
6) If hour = 24 then end day generation.
Conclusion: This FSM will generate unique day, but it is going to follow same patterns.

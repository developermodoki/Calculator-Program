question = input("足し算と引き算、どっちにしますか？ 足し算 = 1 , 引き算 = 2 :")
int_question = int(question)
if int_question == 1 :
    question2 = input("足される数を入力してください。")
    question3 = input("足す数を入力してください。")
    print(int(question2) + int(question3))

if int_question == 2 :
    question4 = input("引かれる数を入力してください。")
    question5 = input("引く数を入力してください。")
    print(int(question4) - int(question5))


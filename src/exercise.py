from payment_card import PaymentCard

def main():
    #write your code below this line
    pauls_card = PaymentCard(20.0)
    matts_card = PaymentCard(30.0)

    pauls_card.eat_heartily()
    matts_card.eat_affordably()
    print("Paul: " + str(pauls_card))
    print("Matt: " + str(matts_card))

    pauls_card.add_money(20.0)
    matts_card.eat_heartily()
    print("Paul: " + str(pauls_card))
    print("Matt: " + str(matts_card))

    pauls_card.eat_affordably()
    pauls_card.eat_affordably()
    matts_card.add_money(50.0)
    print("Paul: " + str(pauls_card))
    print("Matt: " + str(matts_card))

if __name__ == '__main__':
    main()

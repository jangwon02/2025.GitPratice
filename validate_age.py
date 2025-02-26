def validate_age(age):
    if int(age) < 20:
        print("당신은 미성년자군요.")
    else:
        print("당신은 성인이군요.")

if __name__ == "__main__":
    validate_age(20)
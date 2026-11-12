def menu():
    print("【ウチダ電鉄　交通系ICカード検証システム】")
    print("1: 乗車駅選択")
    print("2: チャージ機能")
    try:
       choice = int(input("使用する機能を入力してください(終了する場合には99を入力): "))
    except ValueError:
      print("数字を入力してください。")
      return menu()
    else:
      if choice== 1 or choice == 2 or choice == 99 :
         return choice
      elif choice < 1 or choice > 2:
        print("正しい数値を入力してください。")
        return menu()
    return menu()  

def select_station():
  print("[乗車駅選択]")
  print("  1: 秋葉原駅から    133円 ")
  print("  2: 山梨駅から    4128円 ")
  print("  3: 長野駅から    7990円 ")
  try:
    station = int(input("乗車駅を選択してください(キャンセルする場合には99を入力): "))
  except ValueError:
    print("数字を入力してください。")
    return select_station()
  else:
    if station == 1:
      print("乗車駅は秋葉原で運賃は133円です。")
      return 133
    elif station == 2:
      print("乗車駅は山梨で運賃は4128円です。")
      return 4128
    elif station == 3:
      print("乗車駅は長野で運賃は7990円です。")
      return 7990
    elif station == 99:
      print("駅の選択をキャンセルしました。")
      return 0
    elif station < 1 or station > 3:
      print("正しい数値を入力してください。")
      return select_station()


def pay(zandaka, fare):
  print(f"チャージ残高は{zandaka}円です")
  if zandaka < fare:
    print("残高不足です。")
    while True:
      if zandaka < fare:
        zandaka+=3000
        print("3000円自動チャージします。")
      else:
        break
  zandaka -= fare
  print(f"精算後のチャージ残高は{zandaka}円です")
  while True:
    if zandaka < 500:
      print("残高が500円未満のため3000円自動チャージします。")
      zandaka+=3000
    else:
      print(f"チャージ残高は{zandaka}円です")
      break
  return zandaka


def charge(zandaka):
  print("[チャージ機能]")
  print(f"チャージ残高は{zandaka}円です")
  print("1: 1000円")
  print("2: 2000円")
  print("3: 3000円")
  print("4: 4000円")
  print("5: 5000円")
  print("6: 6000円")
  print("7: 7000円")
  print("8: 8000円")
  print("9: 9000円")
  print("10: 10000円")
  try:
    num = int(input("チャージする金額を選択してください(キャンセルする場合には99を入力): "))
  except ValueError:
    print("数字を入力してください。")
    return charge(zandaka)
  else:
    if num == 1:
      zandaka += 1000
      print("1000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です")
      return zandaka
    elif num == 2:
      zandaka += 2000
      print("2000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です") 
      return zandaka
    elif num == 3:
      zandaka += 3000
      print("3000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です")
      return zandaka
    elif num == 4:
      zandaka += 4000
      print("4000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です")
      return zandaka
    elif num == 5:
      zandaka += 5000
      print("5000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です")
      return zandaka
    elif num == 6:
      zandaka += 6000
      print("6000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です")
      return zandaka
    elif num == 7:
      zandaka += 7000
      print("7000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です")
      return zandaka
    elif num == 8:
      zandaka += 8000
      print("8000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です")
      return zandaka
    elif num == 9:
      zandaka += 9000
      print("9000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です")
      return zandaka
    elif num == 10:
      zandaka += 10000
      print("10000円チャージしました。")
      print(f"チャージ残高は{zandaka}円です")
      return zandaka
    elif num == 99:
      print("チャージをキャンセルしました。")
      return zandaka
    elif num < 1 or num > 10:
      print("正しい数値を入力してください。")
      return charge(zandaka)


def main():
  zandaka = 500
  while True:
    choice = menu()
    if choice == 1:
      fare = select_station()
      if fare != 0:
        zandaka = pay(zandaka, fare)
    elif choice == 2:
      zandaka = charge(zandaka)
    elif choice == 99:
      print("システムを終了します。")
      break


if __name__ == "__main__":
  main()
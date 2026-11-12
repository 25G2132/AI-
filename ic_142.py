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
    return menu()  # 再度メニューを表示するためにmenu()を呼び出す


def select_station():
  station=["秋葉原","山梨県","長野県"]
  fares = [133, 4128, 7990]
  print("乗車駅選択")
  for i in range(len(station)):
    print(f"{i+1}. {station[i]}から{fares[i]}円")
  print("乗車した駅を入力してください(キャンセルする場合には99を入力)")
  destination=int(input())
  if destination==99:
    print("駅の選択をキャンセルしました。")
    return 0
  elif destination==1:
    print(f"乗車駅は{station[destination-1]}で料金は{fares[destination-1]}円です。")
    return fares[destination-1]


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
  while True:
    if zandaka < 500:
      print("残高が500円未満のため3000円自動チャージします。")
      zandaka+=3000
    else:
      break
  print(f"清算後のチャージ残高は{zandaka}円です")
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
      return zandaka
    elif num == 2:
      zandaka += 2000
      print("2000円チャージしました。")
      return zandaka
    elif num == 3:
      zandaka += 3000
      print("3000円チャージしました。")
      return zandaka
    elif num == 4:
      zandaka += 4000
      print("4000円チャージしました。")
      return zandaka
    elif num == 5:
      zandaka += 5000
      print("5000円チャージしました。")
      return zandaka
    elif num == 6:
      zandaka += 6000
      print("6000円チャージしました。")
      return zandaka
    elif num == 7:
      zandaka += 7000
      print("7000円チャージしました。")
      return zandaka
    elif num == 8:
      zandaka += 8000
      print("8000円チャージしました。")
      return zandaka
    elif num == 9:
      zandaka += 9000
      print("9000円チャージしました。")
      return zandaka
    elif num == 10:
      zandaka += 10000
      print("10000円チャージしました。")
      return zandaka
    elif num == 99:
      print("チャージをキャンセルしました。")
      return zandaka
    elif num < 1 or num > 10:
      print("正しい数値を入力してください。")
      return charge(zandaka)


def main():
  zandaka = 500
  #while True:
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  #pass #このpassは処理を書いた後消してよい。


if __name__ == "__main__":
    print("戻り値:", charge(500)) 

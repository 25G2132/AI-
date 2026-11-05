def menu():
    print("【ウチダ電鉄　交通系ICカード検証システム】")
    print("残高：500円")
    print("1: 乗車駅選択")
    print("2: チャージ機能")
    choice = int(input("使用する機能を入力してください(終了する場合には99を入力): "))
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
    return fares[f"{destination-1}"]。


def pay():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def charge():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def main():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


if __name__ == "__main__":
    print("戻り値:", menu()) 

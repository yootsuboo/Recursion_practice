# Data Structure

### リストと配列の違い

- リストは値が連なって見えるがメモリは連続しておらず、各値と次の値へのメモリ参照(ポインタ)を持っており
値が連なっているように見える
- 対して配列はメモリアドレスが連なっている
- メモリアドレスが連なっているため値の増加や削除についてはサポートされていないなどの成約がある(増加はできるが、削除はサポートされていない)
- 連結リストは特定の値に対して削除・追加・挿入がしたい場合は線形検索を実施するデメリットも有る



### 問題一覧

- ソート済連結リストの合併 -> mergeTwoSortedLinkedList.py
- 片方向リストのノードの削除 -> removeNthNode.py
- 連結リストの逆表示 -> reverseLinkedList.py

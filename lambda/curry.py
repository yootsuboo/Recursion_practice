customerList = [
   {
      "id": 1,
      "company": "MH Corp.",
      "name": "Makenzie Hibbert",
      "rank": "A",
      "email": "makenzie@example.com"
   },
   {
      "id": 2,
      "company": "MH Corp.",
      "name": "Abram Martinho Fleming",
      "rank": "B",
      "email": "abram@example.com"
   },
   {
      "id": 3,
      "company": "Best Inc.",
      "name": "Trey Best",
      "rank": "A",
      "email": "trey@example.com"
   },
   {
      "id": 4,
      "company": "Best Inc.",
      "name": "Joshua Charnley",
      "rank": "B",
      "email": "joshua@example.com"
   },
   {
      "id": 5,
      "company": "Best Inc.",
      "name": "Sue Rodger",
      "rank": "C",
      "email": "sue@example.com"
   }
]

# まず、ランクがAの顧客を抽出したい場合、フィルタ関数を使用します。
# filter関数は、配列内の各要素に対してテスト関数（ここではランクが"A"であるかどうかを確認するラムダ式）を適用し、その結果が真である要素だけを新しいリストに入れます。
rankAList = list(filter(lambda customer: customer["rank"] == "A", customerList))
print(rankAList)

# しかしこのフィルタ関数は特定の顧客リストに対してのみ動作します（再利用性がない）。他のリストに対しても適用したい場合、ラムダ式を用いて新しい関数を作ります。
# この新しい関数は配列とランクを受け取り、指定されたランクを以外の要素を抽出します。
extractionByRank = lambda arr, rank: list(filter(lambda customer: customer["rank"] != rank, arr))
print("-----extraction---------")
print(extractionByRank(customerList, "A"))

# 更に高度なフィルタリングを行いたい場合、カリー化という手法を使用できます。
# カリー化は、一つの関数を複数の関数に分割することで、各関数がそれぞれ特定の責任を持つようにする手法です。
# 以下の例では、ランクや会社名でフィルタリングするためのカリー化関数を作成しています。
filterByRank = lambda rank: lambda personal: personal["rank"] == rank
filterByCompany = lambda company: lambda personal: personal["company"] == company

# そして、versatileExtraction関数を作成します。この関数は配列、フィルタリング基準、フィルタリング値を受け取ります。
# この関数は、フィルタリング基準と値を用いてカリー化関数を作り、その関数を配列に適用します。
# このようにすると、多種多様なフィルタリング条件に対応できる非常に汎用性の高い抽出関数を作成できます。
versatileExtraction = lambda arr, filterCriteria, value: list(filter(filterCriteria(value), arr))

print(versatileExtraction(customerList, filterByCompany, "MH Corp."))
print(versatileExtraction(customerList, filterByRank, "A"))

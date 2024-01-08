import math

def longestCommonPrefix(strArr):
    return longestCommonPrefixHelper(strArr, 0, len(strArr) - 1)

def longestCommonPrefixHelper(strArr, start, end):
    if start == end: return strArr[start]

    middle = math.floor((start + end) / 2)
    leftStr = longestCommonPrefixHelper(strArr, start, middle)
    rightStr = longestCommonPrefixHelper(strArr, middle + 1, end)

    return commonPrefix(leftStr, rightStr)

def commonPrefix(leftStr, rightStr):
    # leftStrとrightStrの内、短い方の長さを取得 
    minLen = min(len(leftStr), len(rightStr))
    # 各文字を頭から比較
    for i in range(minLen):
        # i文字目が一致しない場合、leftStrのi文字を返す
        if leftStr[i] != rightStr[i]:
            return leftStr[:i]
    # ループを終了したときは、leftStrのminLen文字を返す
    return leftStr[:minLen]


print(longestCommonPrefix(["ccc", "cbd", "cdc", "c"]))

# ------------------------------------------------------------------------ #
# 要求一：函式與流程控制

def calculate(min, max):
# 請用你的程式補完這個函式的區塊
    sum=0
    for i in range(min,max+1):
        sum+=i
    else:
        print(sum)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30
# ------------------------------------------------------------------------ #
"""
要求一：思路

利用range和變數min、max，產生list，
使用for迴圈跑list，並將list裡的值都加總到sum裡，
在迴圈最後印出sum。
"""
# ------------------------------------------------------------------------ #



# ------------------------------------------------------------------------ #
# 要求二：Python 字典與列表、JavaScript 物件與陣列

def avg(data):
# 請用你的程式補完這個函式的區塊
    e=data["employees"]
    sum=0
    for s in e:
        s1=s["salary"]
        sum+=s1
    else:
        avg_salary=sum/data["count"]
        print(avg_salary)
    
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
}) # 呼叫 avg 函式
# ------------------------------------------------------------------------ #
"""
要求二：思路

先取出data字典裡的employees部分，
用for迴圈讀employees裡的資料，
並把salary的值加總到sum中，
在迴圈最後用sum除以count的值，並印出。
"""
# ------------------------------------------------------------------------ #



# ------------------------------------------------------------------------ #
# 要求三：演算法

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    result=[]
    a=-1
    b=-1
    for i in nums:
        a+=1
        for j in nums:
            b+=1
            if a==b:
                continue
            result+=[i*j]
        else:
            b=-1
    else:
        print(max(result))


maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值
# ------------------------------------------------------------------------ #
"""
要求三：思路

使用兩個for迴圈將list裡的值一一相乘，
同一個位置的數字不進行相乘：使用a和b值代表迴圈跑的位置，相同位置的值就continue不進行相乘，
不同位置的值進行相乘後，將相乘結果放入result裡。（第二個迴圈跑完時，紀錄該迴圈次數的b回到初始值-1，再進入後續的運算。）
迴圈都跑完之後，印出result裡的最大值。
"""
# ------------------------------------------------------------------------ #



# ------------------------------------------------------------------------ #
# 要求四 ( 請閱讀英文 )：演算法

def twoSum(nums, target):
# your code here
    a=-1
    b=-1
    for i in nums:
        a+=1
        for j in nums:
            b+=1
            if a==b:
                continue
            elif i+j==target:
                return [a,b]
                break
        else:
            b=-1
        if i+j==target:
            break
        

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
# ------------------------------------------------------------------------ #
"""
要求四：思路

使用兩個for迴圈將list裡的值一一比較運算，
同一個位置的數字不進行比較運算：使用a和b值代表迴圈跑的位置（該list的位置），相同位置的值就continue不進行比較運算，
若list內兩值相加等於target，函示就回傳[a,b]，並停止第二個迴圈。（第二個迴圈跑完時，紀錄該迴圈次數的b回到初始值-1，再進入後續的運算。）
第一個迴圈最後再檢查一次，若list內兩值相加等於target，就停止第一個迴圈。
"""
# ------------------------------------------------------------------------ #



# ------------------------------------------------------------------------ #
# 要求五 ( Optional )：演算法

def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    a=0
    sum_zero=[0]
    for i in nums:
        if i==1:
            a=0
            continue
        a+=1
        sum_zero+=[a]
    else:
        print(max(sum_zero))


maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
# ------------------------------------------------------------------------ #
"""
要求五：思路

使用for迴圈讀list，
以a值累計讀到0的數量，
當讀到0時，a的次數會加1，並將此數量加入sum_zero中，
當讀到1時，將a累計的數量歸零，並不將此值加入sum_zero中，
迴圈最後，將sum_zero中的最大值印出。
"""
# ------------------------------------------------------------------------ #
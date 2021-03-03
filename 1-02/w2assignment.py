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



# ------------------------------------------------------------------------ #
# 要求三：演算法

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    result=[]
    for i in nums:
        for j in nums:
            if i==j:
                continue
            result+=[i*j]
    else:
        print(max(result))


maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值
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
            if i==j:
                continue
            elif i+j==target:
                break
        return [a,b]

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
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
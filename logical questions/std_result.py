l1 = [['Java',78],["c",86],['math',30],['DBMS',40],['Python',20]]
i=0
while i<len(l1):
      print(l1[i])

      i += 1 

passed = 0

fail = 0
i=0
while i <len(l1):


      sub = l1[i][0]
      marks = l1[i][1]

      if marks >= 40:
            passed += 1
            print(f'{sub} : {marks} : Passed ')
      else :
            fail += 1
            print(f'{sub} : {marks} : Failed ')
      i +=1      

print("Number of subject Passed :",passed)                  
print("Number of subject Fail :",fail) 

if passed == 5 :
      print("Overall : PASS")

else :
      print('Overall : Need Improvement')      







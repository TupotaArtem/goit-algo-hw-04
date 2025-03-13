def total_salary(path):
    try:
        with open(path,encoding='utf-8') as file:
            ls=[]

            for line in file:
                name,cost = line.strip().split(',')
                ls.append(int (cost))

            if not ls:
                return 0, 0   

            total= sum(ls)
            average= total/len(ls)
            
        return total,average
        
    except FileNotFoundError:
        print("Файл не знайдено")  
        return None,None  

    except Exception as e:
        print(f"Невідома помилка {e}")
        return None,None 
def main():
    tot,average=total_salary('/home/tupota/goit-algo-hw-04/text.txt ' )
    print(f"Загальна сума заробітної плати: {tot}, Середня заробітна плата: {average}")

if __name__=='__main__': 
    main()

   
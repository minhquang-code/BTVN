a,b= map(float, input().split())
def dientich(a,b):
    return round(a*b-((min(a,b)*0.5)**2)*3.14, 2)
print(dientich(a,b))
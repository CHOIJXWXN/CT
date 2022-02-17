'''
크로아티아 알파벳
특수한 몇몇 프레이즈는 하나의 문자로 취급하여 총 문자열의 길이를 구하기
모두 replace하여 len함수로 길이를 구해 출력
'''
S = input()
print(len(S.replace('c=', 'a').replace('c-', 'a').replace('dz=', 'a').replace('d-', 'a').replace('lj', 'a').replace('nj', 'a').replace('s=', 'a').replace('z=', 'a')))
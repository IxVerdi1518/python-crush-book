motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
print(motorcycles)

motorcycles.append('ducati')
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print('La última motocicleta que tuve fue la: '+last_owned.title())

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(-2)
print('La última motocicleta que tuve fue la: '+last_owned.title())

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
too_expensive='ducati'
motorcycles.remove(too_expensive)
print('A '+too_expensive.title()+' is too expensive for me.')
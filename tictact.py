import sys

def playT(board):
	isTrue=1
	p1Cor=[]
	p2Cor=[]

	c=0
	whoRunnin=''
	while isTrue:
		c=c+1
		#label:here
		print("Player1: ")
		temp=int(input())
		p1Cor.append(temp)
		print(",",end=" ")
		temp=int(input())
		p1Cor.append(temp)

		print("Player1's ",c," move")
		#if p1Cor[0]<0 or p1Cor[1]>2 or  p2Cor[0]<0 or p2Cor[1]>2:
		#	goto here
		p1F=''.join(str(e) for e in p1Cor)
		board.update({p1F:'X'})
		k=0
		for i in board.values():
			if k %3 == 0:
				print("\n",end=" ")
			print("\t",i,"\t",end=" ")
			k=k+1
		p1Cor.pop()
		p1Cor.pop()
		print("\n")

#label:here
		print("Player2: ")
		temp=int(input())
		p2Cor.append(temp)
		print(",",end=" ")
		temp=int(input())
		p2Cor.append(temp)

		print("Player2's ",c," move")
		#if p1Cor[0]<0 or p1Cor[1]>2 or  p2Cor[0]<0 or p2Cor[1]>2:
		#	goto here
		p2F=''.join(str(e) for e in p2Cor)
		board.update({p2F:'X'})
		k=0
		for i in board.values():
			if k %3 == 0:
				print("\n",end=" ")
			print("\t",i,"\t",end=" ")
			k=k+1
		p2Cor.pop()
		p2Cor.pop()				

		print("\n")
		
		countR=11
		#if  4 > countR > 2  || 14 > countR >12:
		#	countR = countR+8
		if board[countR]==board[countR+1]==board[countR+2]:
			if board[countR]=='X':
				whoRunnin='Player1'
			else:
				whoRunnin="Player2"
			isTrue=0
		elif board[countR]==board[countR+10]==board[countR+20] or board[countR]==board[countR+11]==board[countR+22] :
			if board[countR]=='X':
				whoRunnin='Player1'
			else:
				whoRunnin="Player2"
			isTrue=0
		elif board[countR+2]==board[countR+11]==board[countR+20]:
			if board[countR+2]=='X':
				whoRunnin='Player1'
			else:
				whoRunnin="Player2"
			isTrue=0
		else:
			continue



	print("Game terminated, aand the 'whiner' is: ",whoRunnin)
	print("\nFinally!!:")
	k=1
	for i in board.values():
			if k %3 == 0:
				print("\n",end=" ")
			print("\t",i,"\t",end=" ")
			k=k+1





print("Player1: X")
print("Player2: 0")
board={11:"-",22:"-",33:"-",21:"-",22:"-",23:"-",31:"-",32:"-",33:"-"}
playT(board)

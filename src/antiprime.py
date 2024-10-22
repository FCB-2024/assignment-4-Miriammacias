## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
def main(n) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
		divisors_n=0
		i=1
		while i<=n:
			if n%i==0:
				divisors_n=divisors_n+1
			i=i+1

		j=1
		while j<n:
			divisors_j=0
			k=1
			while k<=j:
				if j%k==0:
					divisors_j=divisors_j+1
				k=k+1
			if divisors_j>=divisors_n:
				return("not anti-prime")
			j=j+1


	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
		return("anti-prime")

## DO NOT REMOVE THIS LINE BELOW
n=int(sys.argv[1])
if __name__ == "__main__" :


	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main(n))

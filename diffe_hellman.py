import math
def diffe_hellman_alice(prime_no, generator, alice_key, bob_key):
    alice =pow(generator,alice_key) % prime_no
    bob =pow(generator,bob_key) % prime_no
    ans1=print(f"so alice's public key is {alice}")
    ans2=print(f"so bob's public key is {bob}")
    shared_key_for_bob = pow(bob,alice_key)% prime_no
    shared_key_for_alice = pow(alice,bob_key) % prime_no
    if shared_key_for_bob == shared_key_for_alice:
        print(f'the encrytion is correct and the shared key is {shared_key_for_bob}!')
    
    return ''
    


def main():
    prime_no = int(input("enter a prime number!\n"))
    generator = int(input("enter (generator) a number b/w 0 and prime_no\n"))
    alice_key = int(input("enter the private key of alice!\n"))
    bob_key = int(input("enter the private key of bob!\n"))
    print(diffe_hellman_alice(prime_no, generator, alice_key, bob_key))
main()

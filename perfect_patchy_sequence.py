def generate_perfect_yf(seq):
  # Create two lists to store the elements of the given sequence
    yf_seq = [i for i in seq if i == "Y" or i == "F"]
    other_seq = [i for i in seq if i not in ["Y", "F"]]
    yf_str = "".join(yf_seq)
    other_str = "".join(other_seq)
    print (f"yf_seq: {yf_str}")
    print (f"other_seq: {other_str}")
  
  # Calculate the number of nodes and blocks
    node = int(len(yf_seq))
    # print (f"node:{node}")
    block = int(len(other_seq) / (node+1))
    # print (f"total length: {len(seq)}")
    # print (f"yf_seq length: {len(yf_seq)}")
    # print (f"other_seq length: {len(other_seq)}")
    # print (f"block: {block}")
  
  # Initialize the list to store the resulting sequence
    perfect_yf = []
  
  # Iterate over the number of nodes
    for i in range(node):
    # Append the first block + 1 elements from the other_seq list
        perfect_yf.extend(other_seq[:int(block)])
        # Append the first element from the yf_seq list
        perfect_yf.append(yf_seq[0])
        # Update the other_seq and yf_seq lists
        other_seq = other_seq[int(block):]
        yf_seq = yf_seq[1:]

        # print ("==============")
        # print (f"loop{i}")
        # print ("perfect_yf:")
        # print ("".join(perfect_yf))
        # print ("other_seq:")
        # print ("".join(other_seq))
        # print ("yf_seq:")
        # print ("".join(yf_seq))
  # Append the remaining elements of the other_seq list
    perfect_yf.extend(other_seq)
    perfect_yf = "".join(perfect_yf)

  
  # Return the resulting sequence
    return perfect_yf

def generate_patchy_yf(seq, patch):
  # Create two lists to store the elements of the given sequence
    yf_seq = [i for i in seq if i == "Y" or i == "F"]
    other_seq = [i for i in seq if i not in ["Y", "F"]]
    # print (yf_seq)
    # print (other_seq)
  
  # Calculate the number of nodes and blocks
    #patch = 5
    num_block_yf = int(len(yf_seq)/patch)
    num_block_other = int(len(other_seq)/(patch+1))
    # print (f"number of yf block: {num_block_yf}")
    # print (f"number of other block: {num_block_other}")


  # Initialize the list to store the resulting sequence
    patchy_yf = []
  # Iterate over the number of nodes
    for i in range(patch):
    # Append the first block + 1 elements from the other_seq list
        patchy_yf.extend(other_seq[:int(num_block_other)])
        # Append the first element from the yf_seq list
        patchy_yf.extend(yf_seq[:int(num_block_yf)])
        # Update the other_seq and yf_seq lists
        other_seq = other_seq[int(num_block_other):]
        yf_seq = yf_seq[int(num_block_yf):]

        # print ("==============")
        # print (f"loop{i}")
        # print ("patchy_yf:")
        # print ("".join(patchy_yf))
        # print ("other_seq:")
        # print ("".join(other_seq))
        # print ("yf_seq:")
        # print ("".join(yf_seq))
  # Append the remaining elements of the other_seq list
    patchy_yf.extend(other_seq)
    patchy_yf = "".join(patchy_yf)

  
  # Return the resulting sequence
    return patchy_yf


# Test the function

seq = "SLENSSNKNEKEKSAPSRTKQTENASQAKQLAELLRLSGPVMQQSQQPQPLQKQPPQPQQQQRPQQQQPHHPQTESVNSYSASGSTNPYMRRPNPVSPYPNSSHTSDIYGSTSPMNFYSTSSQAAGSYLNSSNPMNPYPGLLNQNTQYPSYQCNGNLSVDNCSPYLGSYSPQSQPMDLYRYPSQDPLSKLSLPPIHTLYQPRFGNSQSFTSKYLGYGNQNMQGDGFSSCTIRPNVHHVGKLPPYPTHEMDGHFMGATSRLPPNLSNPNMDYKNGEHHSPSHIIHNYSAAPGMFNSSLHALHLQNKENDMLSHTANGLSKMLPALNHDRTACVQGGLHKLSDANGQEKQPLALVQGVASGAEDN"
seq = list(seq)
patch = 5

print(f"Perfect_YF seq: {generate_perfect_yf(seq)}")
print(f"Final Patchy_YF seq: {generate_patchy_yf(seq, patch)}")

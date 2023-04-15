lines = [
    'local_30._7_1_ == \'p\'',
    'local_48._1_1_ == \'T\'',
    'local_48._7_1_ == \'k\'',
    'local_28._4_1_ == \'d\'',
    '(local_40._3_1_ == \'4\'',
    'local_38._4_1_ == \'e\'',
    'local_40._2_1_ == \'_\'',
    'local_48 == \'H\'',
    'local_28._2_1_ == \'r\'',
    'local_28._3_1_ == \'3\'',
    'local_30._1_1_ == \'_\'',
    'local_48._2_1_ == \'B\'',
    'local_30._5_1_ == \'r\'',
    'local_48._3_1_ == \'{\'',
    'local_30._2_1_ == \'b\'',
    'local_48._5_1_ == \'r\'',
    'local_40._5_1_ == \'4\'',
    'local_30._6_1_ == \'3\'',
    'local_38._3_1_ == \'v\'',
    'local_40._4_1_ == \'p\'',
    'local_28._1_1_ == \'1\'',
    'local_30._3_1_ == \'3\'',
    'local_38._1_1_ == \'n\'',
    'local_48._4_1_ == \'b\'',
    'local_28 == \'4\'',
    'local_40._1_1_ == \'n\'',
    'local_38 == \',\'',
    'local_40 == \'3\'',
    'local_48._6_1_ == \'0\'',
    'local_38._7_1_ == \'t\'',
    'local_40._7_1_ == \'t\'',
    'local_30 == \'0\'',
    'local_40._6_1_ == \'r\'',
    'local_28._5_1_ == \'}\'',
    'local_38._5_1_ == \'r\'',
    'local_38._6_1_ == \'_\'',
    'local_38._2_1_ == \'3\'',
    'local_30._4_1_ == \'_\'',
]

# Step 1: Extract variable names and convert to integers
data = [(int(line.split('_')[1]), line) for line in lines]

# Step 2: Sort variables in ascending order
data = sorted(data)

# Step 3: Create a new list of lines with sorted variables
sorted_lines = [line for (_, line) in data]

# Print the sorted lines
for line in sorted_lines:
    print(line)


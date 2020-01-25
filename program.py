def str_ins(str, i, char):
    return str[:i] + char + str[i:]

def str_replace(str, i, char):
    return str[:i] + char + str[i + 1:]

# Main function
def main():
    # Declaring files
    try:
        inp_s = open("input_src.txt", mode="r", encoding="utf-8")
        inp_d = open("input_dest.txt", mode="r", encoding="utf-8")
    except:
        print("'input_src.txt' or 'input_dest.txt' not exist. Program exiting...")
        return
    outp = open("output.txt", mode="w", encoding="utf-8")


    # Read lines from input files
    inp_s_lines = inp_s.readlines()
    inp_d_lines = inp_d.readlines()

    # Check if 2 files has the same line number
    if (len(inp_s_lines) != len(inp_d_lines)):
        print("The line number of 2 files are different.")
        return
    # Check if each line of 2 files has the same number of dividers (syllable)
    for i in range(0, len(inp_s_lines)):
        src_divs = inp_s_lines[i].count("{")
        des_divs = inp_d_lines[i].count("|") + inp_d_lines[i].count(" ", inp_d_lines[i].find("|"))
        if (src_divs != des_divs):
            print(f"Line number {i + 1} has different quantity of syllable dividers.")
            print(f"Source: {src_divs}\nDestination: {des_divs}")
            print(f"\nSource: {inp_s_lines[i]}")
            print(f"Destination: {inp_d_lines[i]}")
            print("Please correct them before continuing")
            return

    inp_s_tags = []

    # Find tags from input_source
    for i in range(0, len(inp_s_lines)):
        this_line = inp_s_lines[i]
        this_line_tag = []
        start_index = this_line.find("{")
       
        tag_begin = tag_end = start_index
        while (tag_begin != -1 or tag_end != -1):
            tag_begin = this_line.find("{", tag_end)
            tag_end = this_line.find("}", tag_begin)

            if (tag_begin != 1 and tag_end != 1):               
                this_line_tag.append(this_line[tag_begin:tag_end + 1])

        inp_s_tags.append(this_line_tag)

    # Put tags in input_desc
    for i in range(0, len(inp_d_lines)):
        this_line = inp_d_lines[i]
        start_index = this_line.find("|")
        tag_index = 0

        j = start_index

        while (j < len(this_line)):
            if (this_line[j] == " "):
                this_line = str_ins(this_line, j + 1, inp_s_tags[i][tag_index])
                j += len(inp_s_tags[i][tag_index])
                tag_index += 1
            elif (this_line[j] == "|"):
                this_line = str_replace(this_line, j, inp_s_tags[i][tag_index])
                j += len(inp_s_tags[i][tag_index])
                tag_index += 1
            else:
                j += 1
            
        inp_d_lines[i] = this_line 

    # Write lines to output.txt
    outp.writelines(inp_d_lines)
    print("Lines written!")
# Call main function
main()

# Pauses
input("Pausing program")
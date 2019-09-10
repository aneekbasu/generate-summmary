import generate_summary as gs

if __name__ == "__main__":
    top_n = int(input("Enter the number of sentences you want in the summary:"))
    gs.generate_summary( "input.txt",top_n)

######################################################################
# https://leetcode.cn/problems/rearrange-spaces-between-words/
######################################################################

class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_num = 0
        sub_str_list = []
        sub_str = ""
        result_str = ""

        for ch in text:
            if ch == " ":
                space_num += 1
                if sub_str:
                    sub_str_list.append(sub_str)
                    sub_str = ""
            else:
                sub_str += ch
        if sub_str:
            sub_str_list.append(sub_str)

        if len(sub_str_list) == 1:
            sub_str = sub_str_list[0]
            space_str = " "*space_num
            return f"{sub_str}{space_str}"

        insert_space_num = int(space_num/(len(sub_str_list)-1))

        for sub_str in sub_str_list:
            if space_num >= insert_space_num:
                space_str = " "*insert_space_num
            else:
                space_str = " "*space_num
            result_str = f"{result_str}{sub_str}{space_str}"
            space_num -= insert_space_num
        space_str = " "*space_num
        result_str = f"{result_str}{space_str}"

        return result_str
    
if __name__ == "__main__":
    s = Solution()

    text = "  this   is  a sentence "
    print(s.reorderSpaces(text))

    text = " practice   makes   perfect"
    print(s.reorderSpaces(text))

    text = "hello   world"
    print(s.reorderSpaces(text))

    text = "  walks  udp package   into  bar a"
    print(s.reorderSpaces(text))

    text = "a"
    print(s.reorderSpaces(text))

    text = "  hello"
    print(s.reorderSpaces(text))

    text = "a b   c d"
    print(s.reorderSpaces(text))

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
    """
    if user is None or group is None:
        print("user and cannot be null")
        return False

    if type(user) != str:
        print("User must be a string.")
        return False

    if type(group) != Group:
        print("Group does not exist.")
        return False

    if user in group.users:
        return True
    else:
        for group in group.groups:
            return is_user_in_group(user, group)
    return False
            
  
        


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child_user2 = "sub_child_user"

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user2, sub_child))
print(is_user_in_group(sub_child_user, child))
print(is_user_in_group(parent, sub_child))

a=1

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("Test 1", is_user_in_group("","")) # expect 

# Test Case 2
print("Test 2", is_user_in_group(12345,parent)) # expect 

# Test Case 3
print("Test 3", is_user_in_group(None,None)) # expect 





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

    def is_user_in_group(self, user):
        """
        Return True if user is in the group, False otherwise.

        Args:
          user(str): user name/id
          group(class:Group): group to check user membership against
        """
        if user in self.users:
            return True
        for group in self.groups:
            return group.is_user_in_group(user)
        return False



parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child_user2 = "sub_child_user"

child.add_group(sub_child)
parent.add_group(child)

parent.is_user_in_group(sub_child_user2)
a=1

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3






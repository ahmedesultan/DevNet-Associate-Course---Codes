def vendor_list(new_vendor):
    vendors = ["cisco", "juniper", "arista", "huwawi"]
    vendors.append(new_vendor)
    return vendors


x = vendor_list("microsoft")
print(x)

y= vendor_list("amazon")
print(y)

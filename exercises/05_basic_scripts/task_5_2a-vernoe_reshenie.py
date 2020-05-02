inp_sum = input('Input ip address and mask(format x.x.x.x/x): ')
#inp_sum = '10.6.7.8/23'


inp_sep = inp_sum.split('/')

ip_sep = inp_sep[0].split('.')
mask_sep = inp_sep[1]
#print(type(ip_sep))
#print(inp_sep)
#print(ip_sep)
#print(mask_sep)

ip_1, ip_2, ip_3, ip_4 = ip_sep

#print(ip_1)
#print(ip_2)
#print(ip_3)
#print(ip_4)




#mask mask mask mask mask mask mask mask mask mask mask mask



null_count = (32 - int(mask_sep)) * str('0')
mask_bit = '1' * int(mask_sep) + null_count

mask_1 = mask_bit[:8]
mask_2 = mask_bit[8:16]
mask_3 = mask_bit[16:24]
mask_4 = mask_bit[24:]
#print(mask_1)
#print(mask_2)
#print(mask_3)
#print(mask_4)

#######################
# network ip address ##
#######################
# ip_net in dec system
ip_net_1 = int(int(ip_1) & int(mask_1, 2))
ip_net_2 = int(int(ip_2) & int(mask_2, 2))
ip_net_3 = int(int(ip_3) & int(mask_3, 2))
ip_net_4 = int(int(ip_4) & int(mask_4, 2))
#print(ip_net_1)
#print(ip_net_2)
#print(ip_net_3)
#print(ip_net_4)


print('Network:')
templ_ip_dec = '{:<8} {:<8} {:<8} {:<8}'.format(int(ip_net_1), int(ip_net_2), int(ip_net_3), int(ip_net_4))
templ_ip_bin = '{:08b} {:08b} {:08b} {:08b}'.format(int(ip_net_1), int(ip_net_2), int(ip_net_3), int(ip_net_4))
print(templ_ip_dec)
print(templ_ip_bin)


print('Mask:\n/{}'.format(mask_sep))
print('{:<8} {:<8} {:<8} {:<8}'.format(int(mask_1, 2), int(mask_2, 2), int(mask_3, 2), int(mask_4, 2)))
print('{:<8} {:<8} {:<8} {:<8}'.format(mask_1, mask_2, mask_3, mask_4,))

format = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)
list = [format[0].compact, format[1].compact, format[2].compact]
puts list.join(',')

#OR

#puts ARGV[0]
#  .scan(/(?<=from:|to:|flags:).*?(?=\])/)
# .join(',')


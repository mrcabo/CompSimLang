import numpy as np


def write_block(f, block, block_num):
    sInput = "I: {   1} "  # + "{}".format(0)
    sTarget = "T: {   1} "  # + "{}".format(0)
    for i, x in enumerate(block):
        f.write("name: {" + "{}".format(i) + "_{}".format(block_num) + "} 2\n")
        f.write(sInput + "{}".format(x[0]) + '\n')
        f.write(sTarget + "{}".format(x[1]) + '\n')
        f.write(sInput + "{}".format(x[1]) + '\n')
        f.write(sTarget + "{}".format(x[2]) + '\n')
        f.write(";\n")


def write_block2w(f, block, block_num):
    sInput = "I: {   1} "  # + "{}".format(0)
    sTarget = "T: {   1} "  # + "{}".format(0)
    for i, x in enumerate(block):
        f.write("name: {" + "{}".format(i) + "_{}".format(block_num) + "} 3\n")
        f.write(sInput + "{}".format(x[0]) + '\n')
        f.write(sTarget + "{}".format(x[1]) + '\n')
        f.write(sInput + "{}".format(x[1]) + '\n')
        f.write(sTarget + "{}".format(x[2]) + '\n')
        f.write(sInput + "{}".format(x[2]) + '\n')
        f.write(sTarget + "{}".format(x[3]) + '\n')
        f.write(";\n")


def create_block_2w(n_pref, n_word, n_suf):
    prefix_arr = np.arange(n_pref)
    word1_arr = np.arange(n_pref, n_pref+n_word)
    word2_arr = np.copy(word1_arr)
    np.random.shuffle(word2_arr)
    suffix_arr = np.arange(n_pref+n_word, n_pref+n_word+n_suf)

    pref = np.reshape(np.repeat(prefix_arr[0], np.size(word1_arr)), (np.size(word1_arr), 1))
    mid1 = np.reshape(word1_arr, (np.size(word1_arr), 1))
    mid2 = np.reshape(word2_arr, (np.size(word2_arr), 1))
    suf = np.reshape(np.repeat(suffix_arr[0], np.size(word2_arr)), (np.size(word2_arr), 1))
    np.random.shuffle(mid2)
    block = np.hstack((np.hstack((np.hstack((pref, mid1)), mid2)), suf))

    for i in range(1, 3):
        pref = np.reshape(np.repeat(prefix_arr[i], np.size(word1_arr)), (np.size(word1_arr), 1))
        suf = np.reshape(np.repeat(suffix_arr[i], np.size(word1_arr)), (np.size(word1_arr), 1))
        np.random.shuffle(mid2)
        block = np.vstack((block, np.hstack((np.hstack((np.hstack((pref, mid1)), mid2)), suf))))

    # Creating Ungrammatical
    pref = np.reshape(np.repeat(prefix_arr[0], np.size(word1_arr)), (np.size(word1_arr), 1))
    suf1 = np.reshape(np.repeat(suffix_arr[1], np.size(word1_arr)), (np.size(word1_arr), 1))
    suf2 = np.reshape(np.repeat(suffix_arr[2], np.size(word1_arr)), (np.size(word1_arr), 1))
    np.random.shuffle(mid2)
    block_ungr = np.hstack((np.hstack((np.hstack((pref, mid1)), mid2)), suf1))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((np.hstack((pref, mid1)), mid2)), suf2))))
    pref = np.reshape(np.repeat(prefix_arr[1], np.size(word1_arr)), (np.size(word1_arr), 1))
    suf1 = np.reshape(np.repeat(suffix_arr[0], np.size(word1_arr)), (np.size(word1_arr), 1))
    suf2 = np.reshape(np.repeat(suffix_arr[2], np.size(word1_arr)), (np.size(word1_arr), 1))
    np.random.shuffle(mid2)
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((np.hstack((pref, mid1)), mid2)), suf1))))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((np.hstack((pref, mid1)), mid2)), suf2))))
    pref = np.reshape(np.repeat(prefix_arr[2], np.size(word1_arr)), (np.size(word1_arr), 1))
    suf1 = np.reshape(np.repeat(suffix_arr[0], np.size(word1_arr)), (np.size(word1_arr), 1))
    suf2 = np.reshape(np.repeat(suffix_arr[1], np.size(word1_arr)), (np.size(word1_arr), 1))
    np.random.shuffle(mid2)
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((np.hstack((pref, mid1)), mid2)), suf1))))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((np.hstack((pref, mid1)), mid2)), suf2))))

    return block, block_ungr


if __name__ == "__main__":
    # np.random.seed(0)

    train_filename = "q5_train.txt"
    test_filename = "q5_test.txt"
    train2_filename = "q5w2_train.txt"
    test2_filename = "q5w2_test.txt"
    num_prefixes = 3
    num_middle_words = 24
    num_suffixes = 3

    prefix_arr = np.arange(num_prefixes)
    words_arr = np.arange(num_prefixes, num_prefixes+num_middle_words)
    suffix_arr = np.arange(num_prefixes+num_middle_words, num_prefixes+num_middle_words+num_suffixes)
    pref = np.reshape(np.repeat(prefix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    mid = np.reshape(words_arr, (np.size(words_arr), 1))
    suf = np.reshape(np.repeat(suffix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    block = np.hstack((np.hstack((pref, mid)), suf))

    for i in range(1, 3):
        pref = np.reshape(np.repeat(prefix_arr[i], np.size(words_arr)), (np.size(words_arr), 1))
        suf = np.reshape(np.repeat(suffix_arr[i], np.size(words_arr)), (np.size(words_arr), 1))
        block = np.vstack((block, np.hstack((np.hstack((pref, mid)), suf))))

    # Creating Ungrammatical
    pref = np.reshape(np.repeat(prefix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    suf1 = np.reshape(np.repeat(suffix_arr[1], np.size(words_arr)), (np.size(words_arr), 1))
    suf2 = np.reshape(np.repeat(suffix_arr[2], np.size(words_arr)), (np.size(words_arr), 1))
    block_ungr = np.hstack((np.hstack((pref, mid)), suf1))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf2))))
    pref = np.reshape(np.repeat(prefix_arr[1], np.size(words_arr)), (np.size(words_arr), 1))
    suf1 = np.reshape(np.repeat(suffix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    suf2 = np.reshape(np.repeat(suffix_arr[2], np.size(words_arr)), (np.size(words_arr), 1))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf1))))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf2))))
    pref = np.reshape(np.repeat(prefix_arr[2], np.size(words_arr)), (np.size(words_arr), 1))
    suf1 = np.reshape(np.repeat(suffix_arr[0], np.size(words_arr)), (np.size(words_arr), 1))
    suf2 = np.reshape(np.repeat(suffix_arr[1], np.size(words_arr)), (np.size(words_arr), 1))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf1))))
    block_ungr = np.vstack((block_ungr, np.hstack((np.hstack((pref, mid)), suf2))))

    train_file = open(train_filename, 'w')
    for i in range(6):
        np.random.shuffle(block)
        write_block(train_file, block, i)

    np.random.shuffle(block_ungr)
    write_block(train_file, block_ungr, "6")  # Ungrammatical
    np.random.shuffle(block)
    write_block(train_file, block, "7")  # Recovery
    train_file.close()

    # Make the test set
    train_file = open(test_filename, 'w')
    np.random.shuffle(block)
    write_block(train_file, block[0:12], 8)
    train_file.close()

    # Second part
    # block2w, block2w_ungr = create_block_2w(num_prefixes, num_middle_words, num_suffixes)
    # train_file = open(train2_filename, 'w')
    # for i in range(6):
    #     np.random.shuffle(block2w)
    #     write_block2w(train_file, block2w, i)
    # np.random.shuffle(block2w_ungr)
    # write_block2w(train_file, block2w_ungr, "6")  # Ungrammatical
    # np.random.shuffle(block2w)
    # write_block2w(train_file, block2w, "7")  # Recovery
    # train_file.close()
    #
    # # Make the test set
    # train_file = open(test2_filename, 'w')
    # np.random.shuffle(block2w)
    # write_block2w(train_file, block2w[0:12], 8)
    # train_file.close()

    block2w, block2w_ungr = create_block_2w(num_prefixes, num_middle_words, num_suffixes)
    block0_filename = "q5w2_train_block0.ex"
    block1_filename = "q5w2_train_block1.ex"
    block2_filename = "q5w2_train_block2.ex"
    block3_filename = "q5w2_train_block3.ex"
    block4_filename = "q5w2_train_block4.ex"
    block5_filename = "q5w2_train_block5.ex"
    block6_filename = "q5w2_train_block6.ex"
    block7_filename = "q5w2_train_block7.ex"
    # Block 0
    train_file = open(block0_filename, 'w')
    np.random.shuffle(block2w)
    write_block2w(train_file, block2w, 0)
    train_file.close()
    # Block 1
    train_file = open(block1_filename, 'w')
    np.random.shuffle(block2w)
    write_block2w(train_file, block2w, 1)
    train_file.close()
    # Block 2
    train_file = open(block2_filename, 'w')
    np.random.shuffle(block2w)
    write_block2w(train_file, block2w, 2)
    train_file.close()
    # Block 3
    train_file = open(block3_filename, 'w')
    np.random.shuffle(block2w)
    write_block2w(train_file, block2w, 3)
    train_file.close()
    # Block 4
    train_file = open(block4_filename, 'w')
    np.random.shuffle(block2w)
    write_block2w(train_file, block2w, 4)
    train_file.close()
    # Block 5
    train_file = open(block5_filename, 'w')
    np.random.shuffle(block2w)
    write_block2w(train_file, block2w, 5)
    train_file.close()
    # Block ungrammatical
    train_file = open(block6_filename, 'w')
    np.random.shuffle(block2w_ungr)
    write_block2w(train_file, block2w_ungr, "6")  # Ungrammatical
    train_file.close()
    # Block recovery
    train_file = open(block7_filename, 'w')
    np.random.shuffle(block2w)
    write_block2w(train_file, block2w, "7")  # Recovery
    train_file.close()

    # Make the test set
    train_file = open(test2_filename, 'w')
    np.random.shuffle(block2w)
    write_block2w(train_file, block2w[0:12], 8)
    train_file.close()

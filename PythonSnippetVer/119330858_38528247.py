for var in tf.trainable_variables():
    print var.name
    if var.name == 'embedding_rnn_seq2seq/RNN/EmbeddingWrapper/embedding:0':
        embedding_op = var
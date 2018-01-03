from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

sess = tf.InteractiveSession()

# y:模型预测的数字，y_:训练集的数字标签
# 占位符
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])

# 变量
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 变量初始化
sess.run(tf.initialize_all_variables())

# 预测模型
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 损失函数
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# 训练模型
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 加载50个训练样本，训练1000次
for i in range(1000):
    batch = mnist.train.next_batch(50)
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

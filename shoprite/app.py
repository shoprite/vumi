from twisted.python import log
from vumi.application import ApplicationWorker

class ShopriteAppWorker(ApplicationWorker):
  """Application worker class for shoprite vumi app 
  """

  def consume_user_message(self, msg):
      """Pre-process the payload     
      """

      log.msg("User message: %s" % msg['content'])
      log.msg("Object: %s" % msg)

      text = msg['content']

      if text is None:
          reply = self.get_help()
      else:
          reply = self.process_message(text) #process the msg
      self.reply_to(msg, reply)
    
  def process_message(self, text):
    """Main entry point for app """
    log.msg("---PROCESSING---")
    # validate / parse
    if self.validate_msg(text):
      # persist
      f = open('data/data.txt', 'w')
      f.write(text + '\n');
      return "Thank you for your input. We'll let you know when the product is back in stock."
    else:
      # return invalid msg
      return "Invalid message format"

    return "Hello World"

  def validate_msg(self, msg=''):
    return True

  def persist(obj):
    pass

  def get_help(self):
      return "Enter text:"



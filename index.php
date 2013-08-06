<?php

require_once('Wechat.php');


class Remote extends Wechat {

    protected function onSubscribe() {
        $this->resoponseText('Hello, World!');
    }

    protected function onUnsubscribe() {
        $this->resoponseText('Bye :P');
    }

    protected function onText() {
        $this->responseText('大家晚安哇 :) 明天见!');
        #$this->responseText('text msg received: ' .
        #    $this->getRequest('content'));
    }

    protected function onImage() {
        $items = array(
            new NewsResponseItem('标题一', '描述一',
                $this->getRequest('picurl'), $this->getRequest('picurl')),
            new NewsResponseItem('标题二', '描述二',
                $this->getRequest('picurl'), $this->getRequest('picurl')),
        );

        $this->responseNews($items);
    }

    protected function onUnknown() {
        $this->responeText('unknown type msg received: ' .
            $this->getRequest('msgtype'));
    }
}

$config = parse_ini_file('config.ini', 1);

$remote = new Remote($config['wechat']['token'], TRUE);
$remote->run();

/* Copyright 2018 Contributors to Hyperledger Sawtooth

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
----------------------------------------------------------------------------- */


import React, { Component } from 'react';
import { Segment } from 'semantic-ui-react';


import ChatForm from '../forms/ChatForm';
import ChatMessage from './ChatMessage';
import './Chat.css';


import chatTest from '../../mock_data/conversation_action.json';


/**
 *
 * @class Chat
 * Component encapsulating the chat widget
 *
 * TODO: Normalize all JSON objects behind a schema
 *
 */
export default class Chat extends Component {

  /**
   *
   * Switch chat context when active pack changes
   *
   */
  componentWillReceiveProps (newProps) {
    const { activePack, getConversation } = this.props;

    if (newProps.activePack !== activePack) {
      getConversation(newProps.activePack['conversation_id']);
    }
  }


  send (message, action) {
    const { activePack, me, requestAccess, sendMessage } = this.props;

    if (action) {
      const payload = {
        body: action['response_text'],
        from: { id: me.id, name: 'John Doe' }
      };

      console.log(action);
      console.log(payload);
      console.log(activePack);

      sendMessage(payload);

      switch (action.type) {
        case 0:
          requestAccess(activePack.id, me.id, 'some reason');
          break;

        default:
          break;
      }
    }
  }


  render () {
    const { messages } = this.props;

    return (
      <div id='next-chat-container'>
        { messages &&
            <ChatMessage {...this.props}/>
          }

        { messages && messages.length === 0 &&
          <Segment inverted color='violet'>
            Would you like me to request access?
          </Segment>
        }

        <div id='next-chat-conversation-dock'>
          <ChatForm
            actions={chatTest.actions}
            submit={(message, action) => this.send(message, action)}/>
        </div>
      </div>
    );
  }

}

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
import { connect } from 'react-redux';
import { Grid } from 'semantic-ui-react';
import PropTypes from 'prop-types';


import { RequesterSelectors } from '../../redux/RequesterRedux';


import Chat from '../../components/chat/Chat';
import TrackHeader from '../../components/layouts/TrackHeader';
import MemberList from '../../components/layouts/MemberList';


import './Recommended.css';


/**
 *
 * @class Recommended
 * *Recommended* component
 *
 */
export class Recommended extends Component {

  componentDidMount () {
    const { getPack, packId } = this.props;

    if (packId) {
      getPack(packId);
    }
  }


  /**
   *
   * Switch pack on ID change
   *
   *
   */
  componentWillReceiveProps (newProps) {
    const { getPack, packId } = this.props;

    if (newProps.packId !== packId) {
      getPack(newProps.packId);
    }
  }


  render () {
    const { activePack } = this.props;

    if (!activePack) {
      return null;
    }

    return (
      <Grid id='next-requester-grid' celled='internally'>

        <Grid.Column
          id='next-requester-grid-track-column'
          width={10}>
          <TrackHeader title={activePack.name} {...this.props}/>

          <div id='next-requester-recommended-content'>
            <p>Lorem ipsum dolor sit amet.</p>
            <MemberList {...this.props}
              members={activePack.members}
              owners={activePack.owners}/>
          </div>
        </Grid.Column>
        <Grid.Column
          id='next-requester-grid-converse-column'
          width={6}>
          <Chat {...this.props}/>
        </Grid.Column>

      </Grid>
    );
  }

}


Recommended.proptypes = {
  getPack: PropTypes.func,
  activePack: PropTypes.arrayOf(PropTypes.shape(
    {
      name: PropTypes.string
    }
  ))

};


const mapStateToProps = (state, ownProps) => {
  const { params } = ownProps.match;
  const { recommended } = state.requester;

  return {
    packId: RequesterSelectors.idFromSlug(recommended, params.id)
  };
}

const mapDispatchToProps = (dispatch) => {
  return {};
}

export default connect(mapStateToProps, mapDispatchToProps)(Recommended);

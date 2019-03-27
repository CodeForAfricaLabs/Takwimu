import React from 'react';
import PropTypes from 'prop-types';

import { Link, Typography } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';

import takwimu from '../../assets/images/takwimu-logo.png';

const styles = () => ({
  root: {
    width: '19.5625rem'
  },
  text: {
    marginTop: '2.3125rem',
    fontSize: '0.9375rem',
    color: 'white'
  }
});

function StayInTouch({ classes }) {
  return (
    <div className={classes.root}>
      <img src={takwimu} alt="Takwimu" />
      <Typography variant="subtitle2" className={classes.text}>
        Actionable insights for African change makers. Takwimu provides quality
        insights and data-driven analysis to empower African development
        champions.
      </Typography>
      <Typography variant="subtitle2" className={classes.text}>
        <Link href="/about" className={classes.text} underline="always">
          Find out more about us.
        </Link>
      </Typography>
    </div>
  );
}

StayInTouch.propTypes = {
  classes: PropTypes.shape({}).isRequired
};

export default withStyles(styles)(StayInTouch);

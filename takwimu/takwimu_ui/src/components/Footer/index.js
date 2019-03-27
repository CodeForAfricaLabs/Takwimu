import React from 'react';
import PropTypes from 'prop-types';

import { Grid, Typography } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';

import Takwimu from './Takwimu';
import QuickLinks from './QuickLinks';
import StayInTouch from './StayInTouch';
import Initiative from './Initiative';
import Support from './Support';

const styles = theme => ({
  root: {
    flexGrow: 1,
    color: 'white',
    backgroundColor: 'black',
    paddingTop: '4.5625rem',
    paddingBottom: '5.3125rem'
  },
  row: {
    [theme.breakpoints.up('md')]: {
      width: '58.265625rem' // .75 of lg
    },
    [theme.breakpoints.up('lg')]: {
      width: '77.6875rem'
    }
  },
  takwimu: {
    width: '100%',
    [theme.breakpoints.up('md')]: {
      // width: '58.265625rem' // .75 of lg
      marginRight: '2.578125rem'
    },
    [theme.breakpoints.up('lg')]: {
      width: '19.5625rem',
      marginRight: '3.4375rem'
    }
  },
  links: {
    [theme.breakpoints.up('md')]: {
      // width: '58.265625rem' // .75 of lg
      padidngLeft: '4.6875rem',
      paddingRight: '3.9375rem',
      borderLeft: '0.125rem solid rgba(151, 151, 151, 0.45)',
      borderRight: '0.125rem solid rgba(151, 151, 151, 0.45)'
    },
    [theme.breakpoints.up('lg')]: {
      paddingLeft: '6.25rem',
      paddingRight: '5.25rem'
    }
  },
  project: {
    width: '100%',
    [theme.breakpoints.up('md')]: {
      // width: '58.265625rem' // .75 of lg
      marginLeft: '5.109375rem'
    },
    [theme.breakpoints.up('lg')]: {
      width: '19.375rem',
      marginLeft: '6.8125rem'
    }
  }
});

function Footer({ classes }) {
  return (
    <Grid
      container
      className={classes.root}
      justify="center"
      alignItems="flex-start"
    >
      <div className={classes.row}>
        <Grid container justify="flex-start" alignItems="flex-start">
          <div className={classes.takwimu}>
            <Takwimu />
            <StayInTouch />
          </div>
          <div className={classes.links}>
            <QuickLinks />
          </div>
          <div className={classes.project}>
            <Initiative />
            <Support />
          </div>
        </Grid>
      </div>
      <div className={classes.row}>
        <Typography variant="button">2018 Takwimu CC by 4.0</Typography>
      </div>
    </Grid>
  );
}

Footer.propTypes = {
  classes: PropTypes.shape({}).isRequired
};

export default withStyles(styles)(Footer);
